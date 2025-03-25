"""The module.
"""
import math
from typing import List
from needle.autograd import Tensor
from needle import ops
import needle.init as init
import numpy as np
from .nn_basic import Parameter, Module


class Sigmoid(Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: Tensor) -> Tensor:
        return init.ones_like(x) / (1 + ops.exp(-x))


class RNNCell(Module):
    def __init__(self, input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype="float32"):
        """
        Applies an RNN cell with tanh or ReLU nonlinearity.

        Parameters:
        input_size: The number of expected features in the input X
        hidden_size: The number of features in the hidden state h
        bias: If False, then the layer does not use bias weights
        nonlinearity: The non-linearity to use. Can be either 'tanh' or 'relu'.

        Variables:
        W_ih: The learnable input-hidden weights of shape (input_size, hidden_size).
        W_hh: The learnable hidden-hidden weights of shape (hidden_size, hidden_size).
        bias_ih: The learnable input-hidden bias of shape (hidden_size,).
        bias_hh: The learnable hidden-hidden bias of shape (hidden_size,).

        Weights and biases are initialized from U(-sqrt(k), sqrt(k)) where k = 1/hidden_size
        """
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.nonlinearity = ops.tanh if nonlinearity == "tanh" else ops.relu
        self.device = device
        self.dtype = dtype
        self.bias = bias
        self.interval = 1 / math.sqrt(hidden_size)
        self.W_ih = self.init_param(input_size, hidden_size)
        self.W_hh = self.init_param(hidden_size, hidden_size)
        self.bias_ih = self.init_param(hidden_size)
        self.bias_hh = self.init_param(hidden_size)

    def init_param(self, *shape):
        return Parameter(
            init.rand(
                *shape,
                low=-self.interval,
                high=self.interval,
                dtype=self.dtype,
                device=self.device,
            )
        )

    def forward(self, X, h=None):
        """
        Inputs:
        X of shape (bs, input_size): Tensor containing input features
        h of shape (bs, hidden_size): Tensor containing the initial hidden state
            for each element in the batch. Defaults to zero if not provided.

        Outputs:
        h' of shape (bs, hidden_size): Tensor contianing the next hidden state
            for each element in the batch.
        """
        batch = X.shape[0]
        res = X @ self.W_ih
        device = X.device
        dtype = X.dtype
        h = h or init.zeros(batch, self.hidden_size, device=device, dtype=dtype)
        res = res + h @ self.W_hh
        if self.bias:
            bias_ih = ops.broadcast_to(
                self.bias_ih.reshape((1, self.hidden_size)), (batch, self.hidden_size)
            )
            bias_hh = ops.broadcast_to(
                self.bias_hh.reshape((1, self.hidden_size)), (batch, self.hidden_size)
            )
            res = res + bias_ih + bias_hh
        return self.nonlinearity(res)


class RNN(Module):
    def __init__(self, input_size, hidden_size, num_layers=1, bias=True, nonlinearity='tanh', device=None, dtype="float32"):
        """
        Applies a multi-layer RNN with tanh or ReLU non-linearity to an input sequence.

        Parameters:
        input_size - The number of expected features in the input x
        hidden_size - The number of features in the hidden state h
        num_layers - Number of recurrent layers.
        nonlinearity - The non-linearity to use. Can be either 'tanh' or 'relu'.
        bias - If False, then the layer does not use bias weights.

        Variables:
        rnn_cells[k].W_ih: The learnable input-hidden weights of the k-th layer,
            of shape (input_size, hidden_size) for k=0. Otherwise the shape is
            (hidden_size, hidden_size).
        rnn_cells[k].W_hh: The learnable hidden-hidden weights of the k-th layer,
            of shape (hidden_size, hidden_size).
        rnn_cells[k].bias_ih: The learnable input-hidden bias of the k-th layer,
            of shape (hidden_size,).
        rnn_cells[k].bias_hh: The learnable hidden-hidden bias of the k-th layer,
            of shape (hidden_size,).
        """
        super().__init__()
        self.num_layers = num_layers
        self.rnn_cells = [
            RNNCell(
                input_size if k == 0 else hidden_size,
                hidden_size,
                bias=bias,
                nonlinearity=nonlinearity,
                device=device,
                dtype=dtype,
            )
            for k in range(num_layers)
        ]

    def forward(self, X, h0=None):
        """
        Inputs:
        X of shape (seq_len, bs, input_size) containing the features of the input sequence.
        h_0 of shape (num_layers, bs, hidden_size) containing the initial
            hidden state for each element in the batch. Defaults to zeros if not provided.

        Outputs
        output of shape (seq_len, bs, hidden_size) containing the output features
            (h_t) from the last layer of the RNN, for each t.
        h_n of shape (num_layers, bs, hidden_size) containing the final hidden state for each element in the batch.
        """
        hidden_states: List = (
            list(ops.split(h0, axis=0))
            if h0
            else [None for _ in range(self.num_layers)]
        )
        X_split = ops.split(X, axis=0)
        outputs = []
        seq_len = X.shape[0]
        for i in range(seq_len):
            x = X_split[i]
            for j in range(self.num_layers):
                x = self.rnn_cells[j].forward(x, hidden_states[j])
                hidden_states[j] = x
            outputs.append(x)
        return ops.stack(outputs, axis=0), ops.stack(hidden_states, axis=0)


class LSTMCell(Module):
    def __init__(self, input_size, hidden_size, bias=True, device=None, dtype="float32"):
        """
        A long short-term memory (LSTM) cell.

        Parameters:
        input_size - The number of expected features in the input X
        hidden_size - The number of features in the hidden state h
        bias - If False, then the layer does not use bias weights

        Variables:
        W_ih - The learnable input-hidden weights, of shape (input_size, 4*hidden_size).
        W_hh - The learnable hidden-hidden weights, of shape (hidden_size, 4*hidden_size).
        bias_ih - The learnable input-hidden bias, of shape (4*hidden_size,).
        bias_hh - The learnable hidden-hidden bias, of shape (4*hidden_size,).

        Weights and biases are initialized from U(-sqrt(k), sqrt(k)) where k = 1/hidden_size
        """
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.device = device
        self.dtype = dtype
        self.bias = bias
        self.interval = 1 / math.sqrt(hidden_size)
        self.W_ih = self.init_param(input_size, 4 * hidden_size)
        self.W_hh = self.init_param(hidden_size, 4 * hidden_size)
        self.bias_ih = self.init_param(4 * hidden_size)
        self.bias_hh = self.init_param(4 * hidden_size)
        self.sigmoid = Sigmoid()

    def init_param(self, *shape):
        return Parameter(
            init.rand(
                *shape,
                low=-self.interval,
                high=self.interval,
                dtype=self.dtype,
                device=self.device,
            )
        )

    def forward(self, X, h=None):
        """
        Inputs: X, h
        X of shape (batch, input_size): Tensor containing input features
        h, tuple of (h0, c0), with
            h0 of shape (bs, hidden_size): Tensor containing the initial hidden state
                for each element in the batch. Defaults to zero if not provided.
            c0 of shape (bs, hidden_size): Tensor containing the initial cell state
                for each element in the batch. Defaults to zero if not provided.

        Outputs: (h', c')
        h' of shape (bs, hidden_size): Tensor containing the next hidden state for each
            element in the batch.
        c' of shape (bs, hidden_size): Tensor containing the next cell state for each
            element in the batch.
        """
        batch = X.shape[0]
        device = X.device
        dtype = X.dtype
        res = X @ self.W_ih
        if h:
            h0, c0 = h
        else:
            h0 = init.zeros(batch, self.hidden_size, device=device, dtype=dtype)
            c0 = init.zeros(batch, self.hidden_size, device=device, dtype=dtype)
        res = res + h0 @ self.W_hh
        if self.bias:
            bias_ih = ops.broadcast_to(
                self.bias_ih.reshape((1, 4 * self.hidden_size)),
                (batch, 4 * self.hidden_size),
            )
            bias_hh = ops.broadcast_to(
                self.bias_hh.reshape((1, 4 * self.hidden_size)),
                (batch, 4 * self.hidden_size),
            )
            res = res + bias_ih + bias_hh
        res = res.reshape((batch, 4, self.hidden_size))
        i, f, g, o = ops.split(res, axis=1)
        i, f, g, o = self.sigmoid(i), self.sigmoid(f), ops.tanh(g), self.sigmoid(o)
        c = i * g + f * c0
        h = o * ops.tanh(c)
        return h, c


class LSTM(Module):
    def __init__(self, input_size, hidden_size, num_layers=1, bias=True, device=None, dtype="float32"):
        super().__init__()
        """
        Applies a multi-layer long short-term memory (LSTM) RNN to an input sequence.

        Parameters:
        input_size - The number of expected features in the input x
        hidden_size - The number of features in the hidden state h
        num_layers - Number of recurrent layers.
        bias - If False, then the layer does not use bias weights.

        Variables:
        lstm_cells[k].W_ih: The learnable input-hidden weights of the k-th layer,
            of shape (input_size, 4*hidden_size) for k=0. Otherwise the shape is
            (hidden_size, 4*hidden_size).
        lstm_cells[k].W_hh: The learnable hidden-hidden weights of the k-th layer,
            of shape (hidden_size, 4*hidden_size).
        lstm_cells[k].bias_ih: The learnable input-hidden bias of the k-th layer,
            of shape (4*hidden_size,).
        lstm_cells[k].bias_hh: The learnable hidden-hidden bias of the k-th layer,
            of shape (4*hidden_size,).
        """
        super().__init__()
        self.num_layers = num_layers
        self.lstm_cells = [
            LSTMCell(
                input_size if k == 0 else hidden_size,
                hidden_size,
                bias=bias,
                device=device,
                dtype=dtype,
            )
            for k in range(num_layers)
        ]

    def forward(self, X, h=None):
        """
        Inputs: X, h
        X of shape (seq_len, bs, input_size) containing the features of the input sequence.
        h, tuple of (h0, c0) with
            h_0 of shape (num_layers, bs, hidden_size) containing the initial
                hidden state for each element in the batch. Defaults to zeros if not provided.
            c0 of shape (num_layers, bs, hidden_size) containing the initial
                hidden cell state for each element in the batch. Defaults to zeros if not provided.

        Outputs: (output, (h_n, c_n))
        output of shape (seq_len, bs, hidden_size) containing the output features
            (h_t) from the last layer of the LSTM, for each t.
        tuple of (h_n, c_n) with
            h_n of shape (num_layers, bs, hidden_size) containing the final hidden state for each element in the batch.
            h_n of shape (num_layers, bs, hidden_size) containing the final hidden cell state for each element in the batch.
        """
        states: List = [None for _ in range(self.num_layers)]
        if h:
            h0 = ops.split(h[0], axis=0)
            c0 = ops.split(h[1], axis=0)
            for i in range(len((h0))):
                states[i] = (h0[i], c0[i])
        X_split = ops.split(X, axis=0)
        outputs = []
        seq_len = X.shape[0]
        for i in range(seq_len):
            h = X_split[i]
            for j in range(self.num_layers):
                h, c = self.lstm_cells[j].forward(h, states[j])
                states[j] = (h, c)
            outputs.append(h)
        output_pred = ops.stack(outputs, axis=0)
        output_h = ops.stack([s[0] for s in states], axis=0)
        output_c = ops.stack([s[1] for s in states], axis=0)
        return output_pred, (output_h, output_c)


class Embedding(Module):
    def __init__(self, num_embeddings, embedding_dim, device=None, dtype="float32"):
        super().__init__()
        """
        Maps one-hot word vectors from a dictionary of fixed size to embeddings.

        Parameters:
        num_embeddings (int) - Size of the dictionary
        embedding_dim (int) - The size of each embedding vector

        Variables:
        weight - The learnable weights of shape (num_embeddings, embedding_dim)
            initialized from N(0, 1).
        """
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim
        self.weight = Parameter(
            init.randn(
                num_embeddings,
                embedding_dim,
                dtype=dtype,
                device=device,
            )
        )

    def forward(self, x: Tensor) -> Tensor:
        """
        Maps word indices to one-hot vectors, and projects to embedding vectors

        Input:
        x of shape (seq_len, bs)

        Output:
        output of shape (seq_len, bs, embedding_dim)
        """
        onehot = init.one_hot(self.num_embeddings, x, device=x.device)
        T, B, D = onehot.shape
        onehot = onehot.reshape((T * B, D))
        out = onehot @ self.weight
        out = out.reshape((T, B, self.embedding_dim))
        return out
