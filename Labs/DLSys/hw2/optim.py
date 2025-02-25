"""Optimization module"""
import needle as ndl
import numpy as np


class Optimizer:
    def __init__(self, params):
        self.params = params

    def step(self):
        raise NotImplementedError()

    def reset_grad(self):
        for p in self.params:
            p.grad = None


class SGD(Optimizer):
    def __init__(self, params, lr=0.01, momentum=0.0, weight_decay=0.0):
        super().__init__(params)
        self.lr = lr
        self.momentum = momentum
        self.u = {}
        self.weight_decay = weight_decay

    def step(self):
        # 见https://pytorch.org/docs/stable/generated/torch.optim.SGD.html
        # dampening: tao = 1 - beta
        for p in self.params:
            if p not in self.u:
                self.u[p] = ndl.init.zeros_like(p)
            up = self.u[p]
            decayed_grad = p.grad + self.weight_decay * p.data
            up.data = self.momentum * up.data + (1 - self.momentum) * decayed_grad
            p.data = p.data - self.lr * up.data

    def clip_grad_norm(self, max_norm=0.25):
        """
        Clips gradient norm of parameters.
        """
        ### BEGIN YOUR SOLUTION
        raise NotImplementedError()
        ### END YOUR SOLUTION


class Adam(Optimizer):
    def __init__(
        self,
        params,
        lr=0.01,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8,
        weight_decay=0.0,
    ):
        super().__init__(params)
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.weight_decay = weight_decay
        self.t = 0

        self.m = {}
        self.v = {}

    def step(self):
        self.t += 1
        for p in self.params:
            if p not in self.m:
                self.m[p] = ndl.init.zeros_like(p)
                self.v[p] = ndl.init.zeros_like(p)
            mp = self.m[p]
            vp = self.v[p]
            decayed_grad = p.grad + self.weight_decay * p.data

            mp.data = self.beta1 * mp.data + (1 - self.beta1) * decayed_grad
            mp_hat = mp.data / (1 - (self.beta1**self.t))  # 注意，这里不更新到mp.data
            vp.data = self.beta2 * vp.data + (1 - self.beta2) * (decayed_grad**2)
            vp_hat = vp.data / (1 - (self.beta2**self.t))
            p.data = p.data - self.lr * mp_hat / (vp_hat**0.5 + self.eps)
