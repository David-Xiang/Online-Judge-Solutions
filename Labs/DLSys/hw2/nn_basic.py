"""The module.
"""
from typing import List, Callable, Any
from needle.autograd import Tensor
from needle import ops
import needle.init as init
import numpy as np


class Parameter(Tensor):
    """A special kind of tensor that represents parameters."""


def _unpack_params(value: object) -> List[Tensor]:
    if isinstance(value, Parameter):
        return [value]
    elif isinstance(value, Module):
        return value.parameters()
    elif isinstance(value, dict):
        params = []
        for k, v in value.items():
            params += _unpack_params(v)
        return params
    elif isinstance(value, (list, tuple)):
        params = []
        for v in value:
            params += _unpack_params(v)
        return params
    else:
        return []


def _child_modules(value: object) -> List["Module"]:
    if isinstance(value, Module):
        modules = [value]
        modules.extend(_child_modules(value.__dict__))
        return modules
    if isinstance(value, dict):
        modules = []
        for k, v in value.items():
            modules += _child_modules(v)
        return modules
    elif isinstance(value, (list, tuple)):
        modules = []
        for v in value:
            modules += _child_modules(v)
        return modules
    else:
        return []


class Module:
    def __init__(self):
        self.training = True

    def parameters(self) -> List[Tensor]:
        """Return the list of parameters in the module."""
        return _unpack_params(self.__dict__)

    def _children(self) -> List["Module"]:
        return _child_modules(self.__dict__)

    def eval(self):
        self.training = False
        for m in self._children():
            m.training = False

    def train(self):
        self.training = True
        for m in self._children():
            m.training = True

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)


class Identity(Module):
    def forward(self, x):
        return x


class Linear(Module):
    def __init__(
        self, in_features, out_features, bias=True, device=None, dtype="float32"
    ):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features

        self.weight = Parameter(
            init.kaiming_uniform(in_features, out_features, dtype=dtype)
        )
        self.bias = (
            Parameter(init.kaiming_uniform(out_features, 1, dtype=dtype).transpose())
            if bias
            else None
        )

    def forward(self, X: Tensor) -> Tensor:
        res = X @ self.weight
        if self.bias:
            batch_size = X.shape[0]
            res = res + ops.broadcast_to(self.bias, res.shape)
        return res


class Flatten(Module):
    def forward(self, X):
        batch_size = X.shape[0]
        channels = 1
        for i, c in enumerate(X.shape):
            if i == 0:
                continue
            channels *= c
        return ops.reshape(X, (batch_size, channels))


class ReLU(Module):
    def forward(self, x: Tensor) -> Tensor:
        return ops.relu(x)


class Sequential(Module):
    def __init__(self, *modules):
        super().__init__()
        self.modules = modules

    def forward(self, x: Tensor) -> Tensor:
        for m in self.modules:
            x = m(x)
        return x


class SoftmaxLoss(Module):
    def forward(self, logits: Tensor, y: Tensor):
        batch_size, num_classes = logits.shape
        lossumexp = ops.logsumexp(logits, axes=(1,))
        logit_true = ops.summation(logits * init.one_hot(num_classes, y), axes=(1,))
        sum_loss = ops.summation(lossumexp - logit_true)
        loss = sum_loss / batch_size
        return loss


class BatchNorm1d(Module):
    def __init__(self, dim, eps=1e-5, momentum=0.1, device=None, dtype="float32"):
        super().__init__()
        self.dim = dim
        self.eps = eps
        self.momentum = momentum
        self.weight = Parameter(init.ones(dim, dtype=dtype))
        self.bias = Parameter(init.zeros(dim, dtype=dtype))
        self.running_mean = init.zeros(dim, dtype=dtype)
        self.running_var = init.ones(dim, dtype=dtype)

    def running_estimate(self, old_t, new_t):
        return (1 - self.momentum) * old_t.data + self.momentum * new_t.data

    def forward(self, x: Tensor) -> Tensor:
        weight_2d = ops.broadcast_to(self.weight, x.shape)
        bias_2d = ops.broadcast_to(self.bias, x.shape)

        if not self.training:
            mu = self.running_mean
            sigma = (self.running_var + self.eps) ** (1 / 2)
            mu_2d = ops.broadcast_to(mu, x.shape)
            sigma_2d = ops.broadcast_to(sigma, x.shape)
            return weight_2d * ((x - mu_2d) / sigma_2d) + bias_2d

        batch_size = x.shape[0]
        x_mean = ops.summation(x, axes=(0,)) / batch_size
        x_mean_2d = ops.broadcast_to(ops.reshape(x_mean, (1, self.dim)), x.shape)
        x_var = ops.summation((x - x_mean_2d) ** 2, axes=(0,)) / batch_size
        x_std = (x_var + self.eps) ** (1 / 2)
        x_std_2d = ops.broadcast_to(ops.reshape(x_std, (1, self.dim)), x.shape)
        self.running_mean.data = self.running_estimate(
            self.running_mean.data, x_mean.data
        )
        self.running_var.data = self.running_estimate(self.running_var.data, x_var.data)
        return weight_2d * ((x - x_mean_2d) / x_std_2d) + bias_2d


class LayerNorm1d(Module):
    def __init__(self, dim, eps=1e-5, device=None, dtype="float32"):
        super().__init__()
        self.dim = dim
        self.eps = eps
        self.weight = Parameter(init.ones(dim, dtype=dtype))
        self.bias = Parameter(init.zeros(dim, dtype=dtype))

    def forward(self, x: Tensor) -> Tensor:
        batch_size = x.shape[0]
        x_mean = ops.summation(x, axes=(1,)) / self.dim
        x_mean_2d = ops.broadcast_to(ops.reshape(x_mean, (batch_size, 1)), x.shape)
        x_var = ops.summation((x - x_mean_2d) ** 2, axes=(1,)) / self.dim
        x_std = (x_var + self.eps) ** (1 / 2)
        x_std_2d = ops.broadcast_to(ops.reshape(x_std, (batch_size, 1)), x.shape)
        weight_2d = ops.broadcast_to(self.weight, x.shape)
        bias_2d = ops.broadcast_to(self.bias, x.shape)
        return weight_2d * ((x - x_mean_2d) / x_std_2d) + bias_2d


class Dropout(Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p

    def forward(self, x: Tensor) -> Tensor:
        if not self.training:
            return x
        rand = Tensor(init.randb(*x.shape, p=1 - self.p))
        return x * rand / (1 - self.p)


class Residual(Module):
    def __init__(self, fn: Module):
        super().__init__()
        self.fn = fn

    def forward(self, x: Tensor) -> Tensor:
        return self.fn(x) + x
