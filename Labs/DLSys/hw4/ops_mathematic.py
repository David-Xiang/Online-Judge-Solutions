"""Operator implementations."""

from numbers import Number
from typing import Optional, List, Tuple, Union

from ..autograd import NDArray
from ..autograd import Op, Tensor, Value, TensorOp
from ..autograd import TensorTuple, TensorTupleOp
import numpy

# NOTE: we will import numpy as the array_api
# as the backend for our computations, this line will change in later homeworks

from ..backend_selection import array_api, BACKEND
from .ops_tuple import *


class EWiseAdd(TensorOp):
    def compute(self, a: NDArray, b: NDArray):
        assert a.shape == b.shape
        return a + b

    def gradient(self, out_grad: Tensor, node: Tensor):
        return out_grad, out_grad


def add(a, b):
    return EWiseAdd()(a, b)


class AddScalar(TensorOp):
    def __init__(self, scalar):
        self.scalar = scalar

    def compute(self, a: NDArray):
        return array_api.add(a, self.scalar, dtype=a.dtype)

    def gradient(self, out_grad: Tensor, node: Tensor):
        return out_grad


def add_scalar(a, scalar):
    return AddScalar(scalar)(a)


class EWiseMul(TensorOp):
    def compute(self, a: NDArray, b: NDArray):
        assert a.shape == b.shape
        return a * b

    def gradient(self, out_grad: Tensor, node: Tensor):
        lhs, rhs = node.inputs
        return out_grad * rhs, out_grad * lhs


def multiply(a, b):
    return EWiseMul()(a, b)


class MulScalar(TensorOp):
    def __init__(self, scalar):
        self.scalar = scalar

    def compute(self, a: NDArray):
        return array_api.multiply(a, self.scalar, dtype=a.dtype)

    def gradient(self, out_grad: Tensor, node: Tensor):
        return out_grad * self.scalar


def mul_scalar(a, scalar):
    return MulScalar(scalar)(a)


class EWisePow(TensorOp):
    """Op to element-wise raise a tensor to a power."""

    def compute(self, a: NDArray, b: NDArray) -> NDArray:
        assert a.shape == b.shape
        return a**b

    def gradient(self, out_grad, node):
        a, b = node.inputs
        # a_grad = multiply(out_grad, multiply(b, power(a, add_scalar(b, -1))))
        # b_grad = multiply(out_grad, multiply(log(a), power(a, b)))
        a_grad = out_grad * b * a ** (b - 1)
        b_grad = out_grad * log(a) * a**b
        return a_grad, b_grad


def power(a, b):
    return EWisePow()(a, b)


class PowerScalar(TensorOp):
    """Op raise a tensor to an (integer) power."""

    def __init__(self, scalar: int):
        self.scalar = scalar

    def compute(self, a: NDArray) -> NDArray:
        return array_api.power(a, self.scalar, dtype=a.dtype)

    def gradient(self, out_grad, node):
        # return multiply(
        #     out_grad,
        #     mul_scalar(power_scalar(node.inputs[0], self.scalar - 1), self.scalar),
        # )
        return out_grad * (node.inputs[0] ** (self.scalar - 1)) * self.scalar


def power_scalar(a, scalar):
    return PowerScalar(scalar)(a)


class EWiseDiv(TensorOp):
    """Op to element-wise divide two nodes."""

    def compute(self, a, b):
        assert a.shape == b.shape
        return a / b

    def gradient(self, out_grad, node):
        a, b = node.inputs
        # grad_a = divide(out_grad, b)
        # grad_b = multiply(out_grad, negate(multiply(a, power_scalar(b, -2))))
        return out_grad / b, out_grad * -(a * (b**-2))


def divide(a, b):
    return EWiseDiv()(a, b)


class DivScalar(TensorOp):
    def __init__(self, scalar):
        self.scalar = scalar

    def compute(self, a):
        return array_api.divide(a, self.scalar, dtype=a.dtype)

    def gradient(self, out_grad, node):
        # return divide_scalar(out_grad, self.scalar)
        return out_grad / self.scalar


def divide_scalar(a, scalar):
    return DivScalar(scalar)(a)


class Transpose(TensorOp):
    def __init__(self, axes: Optional[tuple] = None):
        self.axes = axes

    def compute(self, a):
        if self.axes:
            swap_axes = {self.axes[0]: self.axes[1], self.axes[1]: self.axes[0]}
        else:
            swap_axes = {a.ndim - 1: a.ndim - 2, a.ndim - 2: a.ndim - 1}
        permutation = [swap_axes[i] if i in swap_axes else i for i in range(a.ndim)]
        return array_api.transpose(a, axes=permutation)

    def gradient(self, out_grad, node):
        return transpose(out_grad, axes=self.axes)


def transpose(a, axes=None):
    return Transpose(axes)(a)


class Reshape(TensorOp):
    def __init__(self, shape):
        self.shape = shape

    def compute(self, a):
        return array_api.reshape(a, self.shape)

    def gradient(self, out_grad, node):
        return reshape(out_grad, node.inputs[0].shape)


def reshape(a, shape):
    return Reshape(shape)(a)


class BroadcastTo(TensorOp):
    def __init__(self, shape):
        self.shape = shape

    def compute(self, a):
        if self.shape == a.shape:
            return a
        return array_api.broadcast_to(a, self.shape)

    def gradient(self, out_grad, node):
        input_shape = node.inputs[0].shape  # (m,1,p)
        output_shape = self.shape  # (k,m,n,p)
        if input_shape == output_shape:
            return out_grad
        dim_diff = len(output_shape) - len(input_shape)
        normalize_input_shape = (1,) * dim_diff + input_shape  # (1,m,1,p)
        broadcasted_axes = tuple(
            [
                i
                for i in range(len(output_shape))
                if normalize_input_shape[i] == 1 and output_shape[i] != 1
            ]
        )  # (0, 2)
        sum = summation(out_grad, broadcasted_axes)
        reshaped = reshape(sum, input_shape)
        return reshaped


def broadcast_to(a, shape):
    return BroadcastTo(shape)(a)


class Summation(TensorOp):
    def __init__(self, axes: Optional[tuple] = None):
        self.axes = axes

    def compute(self, a):
        # axes = [0], m,n,p -> n,p
        if not self.axes:
            return array_api.sum(a)
        for axis in reversed(sorted(self.axes)):
            a = array_api.sum(a, axis=axis)
        return a

    def gradient(self, out_grad, node):
        input_shape = node.inputs[0].shape  # (m,n,p)
        axes = self.axes or tuple(
            range(len(input_shape))
        )  # axes为None表示对所有axes求和
        # 如果在某个axe上求和，那梯度就要broadcast到这个axe的每一个分量
        normalized_shape = tuple(
            [1 if i in axes else input_shape[i] for i in range(len(input_shape))]
        )  # (1,n,p)
        return broadcast_to(
            reshape(out_grad, normalized_shape), input_shape
        )  # broadcast 1,n,p -> m,n,p


def summation(a, axes=None):
    if isinstance(axes, int):  # hw4 test case问题
        axes = (axes,)
    return Summation(axes)(a)


class MatMul(TensorOp):
    def compute(self, a, b):
        # (m, n) * (n, k) -> (m, k)
        # (t, m, n) * (t, n, k) -> (t, m, k)
        # (t, m, n) * (n, k) -> (t, m, k)
        return a @ b

    def gradient(self, out_grad: Tensor, node):
        a, b = node.inputs
        # grad_a = matmul(out_grad, transpose(b))
        # grad_b = matmul(transpose(a), out_grad)
        grad_a = out_grad @ transpose(b)
        grad_b = transpose(a) @ out_grad
        if len(out_grad.shape) > len(a.shape):
            reduce_dim = len(out_grad.shape) - len(a.shape)
            grad_a = summation(grad_a, axes=tuple(range(reduce_dim)))
        if len(out_grad.shape) > len(b.shape):
            reduce_dim = len(out_grad.shape) - len(b.shape)
            grad_b = summation(grad_b, axes=tuple(range(reduce_dim)))
        return grad_a, grad_b


def matmul(a, b):
    return MatMul()(a, b)


class Negate(TensorOp):
    def compute(self, a):
        return -a

    def gradient(self, out_grad, node):
        # return negate(out_grad)
        return -out_grad


def negate(a):
    return Negate()(a)


class Log(TensorOp):
    def compute(self, a):
        return array_api.log(a)

    def gradient(self, out_grad, node):
        # return multiply(out_grad, power_scalar(node.inputs[0], -1))
        return out_grad * (node.inputs[0] ** -1)


def log(a):
    return Log()(a)


class Exp(TensorOp):
    def compute(self, a):
        return array_api.exp(a)

    def gradient(self, out_grad, node):
        # return multiply(out_grad, exp(node.inputs[0]))
        return out_grad * node


def exp(a):
    return Exp()(a)


class ReLU(TensorOp):
    def compute(self, a):
        return array_api.maximum(a, 0)

    def gradient(self, out_grad, node):
        cache_data = node.realize_cached_data()
        mask = Tensor(cache_data > 0, device=node.device)
        return mask * out_grad


def relu(a):
    return ReLU()(a)


class Tanh(TensorOp):
    def compute(self, a):
        return a.tanh()

    def gradient(self, out_grad, node):
        return out_grad * (-(node**2) + 1)


def tanh(a):
    return Tanh()(a)


class Stack(TensorOp):
    def __init__(self, axis: int):
        """
        Concatenates a sequence of arrays along a new dimension.
        Parameters:
        axis - dimension to concatenate along
        All arrays need to be of the same size.
        """
        self.axis = axis

    def compute(self, args: TensorTuple) -> Tensor:
        len_tuples = len(args)
        shape = args[0].shape
        device = args[0].device

        stack_shape = [*shape]
        stack_shape.insert(self.axis, len_tuples)
        arr_shape = [*shape]
        arr_shape.insert(self.axis, 1)

        stacked = NDArray.make(stack_shape, device=device)
        for i, arr in enumerate(args):
            idxs = [slice(None) for _ in shape]
            idxs.insert(self.axis, slice(i, i + 1, 1))
            stacked[tuple(idxs)] = arr.reshape(arr_shape)
        return stacked

    def gradient(self, out_grad, node):
        return split(out_grad, node.op.axis)


def stack(args, axis):
    return Stack(axis)(make_tuple(*args))


class Split(TensorTupleOp):
    def __init__(self, axis: int):
        """
        Splits a tensor along an axis into a tuple of tensors.
        (The "inverse" of Stack)
        Parameters:
        axis - dimension to split
        """
        self.axis = axis

    def compute(self, A):
        len_tuples = A.shape[self.axis]
        arr_shape = A.shape[: self.axis] + A.shape[self.axis + 1 :]
        arrs = []

        for i in range(len_tuples):
            idxs = [slice(None) for _ in range(len(A.shape) - 1)]
            idxs.insert(self.axis, slice(i, i + 1, 1))
            arr = A[tuple(idxs)].reshape(arr_shape)
            arrs.append(arr)
        return tuple(arrs)

    def gradient(self, out_grad, node):
        return stack(out_grad, node.op.axis)


def split(a, axis):
    return Split(axis)(a)


class Flip(TensorOp):
    def __init__(self, axes: Optional[tuple] = None):
        self.axes = axes

    def compute(self, a):
        return array_api.flip(a, self.axes)

    def gradient(self, out_grad, node):
        return flip(out_grad, self.axes)


def flip(a, axes):
    return Flip(axes)(a)


class Dilate(TensorOp):
    def __init__(self, axes: tuple, dilation: int):
        self.axes = axes
        self.dilation = dilation

    def compute(self, a):
        if self.dilation == 0:
            return a
        step = self.dilation + 1
        new_shape = [s * step if i in self.axes else s for i, s in enumerate(a.shape)]
        dilated = array_api.full(new_shape, 0, device=a.device)
        idxs = tuple(
            [
                slice(0, None, step) if i in self.axes else slice(0, None)
                for i, s in enumerate(a.shape)
            ]
        )
        dilated[idxs] = a
        return dilated

    def gradient(self, out_grad, node):
        return undilate(out_grad, self.axes, self.dilation)


def dilate(a, axes, dilation):
    return Dilate(axes, dilation)(a)


class UnDilate(TensorOp):
    def __init__(self, axes: tuple, dilation: int):
        self.axes = axes
        self.dilation = dilation

    def compute(self, a):
        if self.dilation == 0:
            return a
        step = self.dilation + 1
        new_shape = [s // step if i in self.axes else s for i, s in enumerate(a.shape)]
        new_strides = [
            s * step if i in self.axes else s for i, s in enumerate(a.strides)
        ]
        return NDArray.make(
            new_shape,
            strides=new_strides,
            device=a.device,
            handle=a._handle,
            offset=a._offset,
        )

    def gradient(self, out_grad, node):
        return undilate(out_grad, self.axes, self.dilation)


def undilate(a, axes, dilation):
    return UnDilate(axes, dilation)(a)


class Conv(TensorOp):
    def __init__(self, stride: Optional[int] = 1, padding: Optional[int] = 0):
        self.stride = stride
        self.padding = padding

    def compute(self, A, B):
        # A = NHWI, B = KKIO
        A = A.pad(
            ((0, 0), (self.padding, self.padding), (self.padding, self.padding), (0, 0))
        )
        N, H, W, C_in = A.shape
        Ns, Hs, Ws, Cs = A.strides
        K, _, _, C_out = B.shape
        H_out = (H - K) // self.stride + 1
        W_out = (W - K) // self.stride + 1
        new_shape = (N, H_out, W_out, K, K, C_in)
        new_strides = (Ns, Hs * self.stride, Ws * self.stride, Hs, Ws, Cs)
        A = A.as_strided(new_shape, new_strides).compact()
        A = A.reshape((N * H_out * W_out, K * K * C_in))
        B = B.reshape((K * K * C_in, C_out))
        out = A @ B
        out = out.reshape((N, H_out, W_out, C_out))
        return out

    def gradient(self, out_grad, node):  # NH'W'O
        A, B = node.inputs[0], node.inputs[1]  # NHWI, KKIO
        N, H, W, C_in = A.shape
        K, _, _, C_out = B.shape
        if self.stride != 1:
            out_grad = dilate(out_grad, axes=(1, 2), dilation=self.stride - 1)

        B_t = flip(B, axes=(0, 1))  # flip kernel
        B_t = transpose(B_t, axes=(2, 3))  # KKOI
        X_grad = conv(
            out_grad, B_t, padding=K - 1 - self.padding
        )  # NH'W'I, KKOI -> NHWI

        A_t = transpose(A, axes=(0, 3))  # IHWN
        O_t = transpose(transpose(out_grad, (0, 1)), (1, 2))  # H'W'NO
        W_grad_t = conv(A_t, O_t, padding=self.padding)  # IHWN, H'W'NO -> IKKO
        W_grad = transpose(transpose(W_grad_t, (0, 1)), (1, 2))  # KKIO
        return X_grad, W_grad


def conv(a, b, stride=1, padding=1):
    return Conv(stride, padding)(a, b)


