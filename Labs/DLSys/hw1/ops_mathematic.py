"""Operator implementations."""

from numbers import Number
from typing import Optional, List, Tuple, Union

from ..autograd import NDArray
from ..autograd import Op, Tensor, Value, TensorOp
from ..autograd import TensorTuple, TensorTupleOp
import numpy

# NOTE: we will import numpy as the array_api
# as the backend for our computations, this line will change in later homeworks

BACKEND = "np"
import numpy as array_api

class EWiseAdd(TensorOp):
    def compute(self, a: NDArray, b: NDArray):
        return a + b

    def gradient(self, out_grad: Tensor, node: Tensor):
        return out_grad, out_grad


def add(a, b):
    return EWiseAdd()(a, b)


class AddScalar(TensorOp):
    def __init__(self, scalar):
        self.scalar = scalar

    def compute(self, a: NDArray):
        return a + self.scalar

    def gradient(self, out_grad: Tensor, node: Tensor):
        return out_grad


def add_scalar(a, scalar):
    return AddScalar(scalar)(a)


class EWiseMul(TensorOp):
    def compute(self, a: NDArray, b: NDArray):
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
        return a * self.scalar

    def gradient(self, out_grad: Tensor, node: Tensor):
        return (out_grad * self.scalar,)


def mul_scalar(a, scalar):
    return MulScalar(scalar)(a)


class EWisePow(TensorOp):
    """Op to element-wise raise a tensor to a power."""

    def compute(self, a: NDArray, b: NDArray) -> NDArray:
        return array_api.power(a, b)

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
        return array_api.power(a, self.scalar)

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
        return array_api.divide(a, b)

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
        return array_api.divide(a, self.scalar)

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
        return array_api.broadcast_to(a, self.shape)

    def gradient(self, out_grad, node):
        input_shape = node.inputs[0].shape  # (m,1,p)
        output_shape = self.shape  # (k,m,n,p)
        dim_diff = len(output_shape) - len(input_shape)
        normalize_input_shape = (1,) * dim_diff + input_shape  # (1,m,1,p)
        broadcasted_axes = tuple(
            [
                i
                for i in range(len(output_shape))
                if normalize_input_shape[i] == 1 and output_shape[i] != 1
            ]
        )  # (0, 2)
        return reshape(summation(out_grad, broadcasted_axes), input_shape)


def broadcast_to(a, shape):
    return BroadcastTo(shape)(a)


class Summation(TensorOp):
    def __init__(self, axes: Optional[tuple] = None):
        self.axes = axes

    def compute(self, a):
        # axes = [0], m,n,p -> n,p
        res =  array_api.sum(a, axis=self.axes)
        return res

    def gradient(self, out_grad, node):
        input_shape = node.inputs[0].shape  # (m,n,p)
        axes = self.axes or tuple(range(len(input_shape))) # axes为None表示对所有axes求和
        # 如果在某个axe上求和，那梯度就要broadcast到这个axe的每一个分量
        normalized_shape = tuple(
            [1 if i in axes else input_shape[i] for i in range(len(input_shape))]
        )  # (1,n,p)
        return broadcast_to(
            reshape(out_grad, normalized_shape), input_shape
        )  # broadcast 1,n,p -> m,n,p


def summation(a, axes=None):
    return Summation(axes)(a)


class MatMul(TensorOp):
    def compute(self, a, b):
        # (m, n) * (n, k) -> (m, k)
        # (t, m, n) * (t, n, k) -> (t, m, k)
        # (t, m, n) * (n, k) -> (t, m, k)
        return array_api.matmul(a, b)

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
        return array_api.negative(a)

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
        return out_grad * exp(node.inputs[0])


def exp(a):
    return Exp()(a)


class ReLU(TensorOp):
    def compute(self, a):
        return array_api.maximum(a, 0)

    def gradient(self, out_grad, node):
        cache_data = node.realize_cached_data()
        mask = Tensor(array_api.float32(cache_data > 0))
        return mask * out_grad


def relu(a):
    return ReLU()(a)

