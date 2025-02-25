from typing import Optional
from ..autograd import NDArray
from ..autograd import Op, Tensor, Value, TensorOp
from ..autograd import TensorTuple, TensorTupleOp

from .ops_mathematic import *

import numpy as array_api

class LogSoftmax(TensorOp):
    def compute(self, Z):
        assert len(Z.shape) == 2
        Z_max = array_api.max(Z, axis=1, keepdims=True)
        Z_max_broadcast = array_api.broadcast_to(Z_max, Z.shape)
        exp = array_api.exp(Z - Z_max)
        exp_sum = array_api.broadcast_to(
            array_api.sum(exp, axis=1, keepdims=True), Z.shape
        )
        return (
            Z - Z_max_broadcast - array_api.log(exp_sum)
        )  # 只能用最后一个等式的计算方法

    def gradient(self, out_grad, node):
        # 这个题check了很久始终不对，需要注意的是x_i对于任何一个y_j都有作用
        # 因此需要out_grad梯度进行累加，而不是一对一
        Z: Tensor = node.inputs[0]
        normalized_shape = (Z.shape[0], 1)
        Z_max = broadcast_to(reshape(max(Z, axes=1), normalized_shape), Z.shape)
        sum_exp = broadcast_to(
            reshape(summation(exp(Z - Z_max), 1), normalized_shape), Z.shape
        )
        softmax = exp(Z - Z_max) / sum_exp
        out_grad_sum = broadcast_to(
            reshape(summation(out_grad, 1), (Z.shape[0], 1)), Z.shape
        )
        return out_grad - softmax * out_grad_sum


def logsoftmax(a):
    return LogSoftmax()(a)


class Max(TensorOp):
    def __init__(self, axes: Optional[tuple] = None):
        self.axes = axes

    def compute(self, Z):
        return array_api.max(Z, axis=self.axes)


def max(a, axes=None):
    return Max(axes)(a)


class LogSumExp(TensorOp):
    def __init__(self, axes: Optional[tuple] = None):
        self.axes = axes

    def compute(self, Z):
        axes = self.axes or tuple(range(len(Z.shape)))
        normalized_shape = tuple(
            [1 if i in axes else Z.shape[i] for i in range(len(Z.shape))]
        )
        Z_max = array_api.max(Z, self.axes)
        Z_max_reshape = array_api.reshape(Z_max, normalized_shape)
        exp_sum = array_api.sum(array_api.exp(Z - Z_max_reshape), axis=self.axes)
        return array_api.log(exp_sum) + Z_max

    def gradient(self, out_grad, node):
        # 先化为不带max的函数求梯度，再考虑数值稳定问题
        Z: Tensor = node.inputs[0]
        axes = self.axes or tuple(range(len(Z.shape)))
        normalized_shape = tuple(
            [1 if i in axes else Z.shape[i] for i in range(len(Z.shape))]
        )
        # 这里的shape通通用reshape + broadcast_to显式处理，禁止隐式转换
        broadcast_out_grad = broadcast_to(reshape(out_grad, normalized_shape), Z.shape)
        Z_max = broadcast_to(reshape(max(Z, axes), normalized_shape), Z.shape)
        grad = exp(Z - Z_max) / broadcast_to(
            reshape(summation(exp(Z - Z_max), self.axes), normalized_shape), Z.shape
        )
        return broadcast_out_grad * grad


def logsumexp(a, axes=None):
    return LogSumExp(axes=axes)(a)

