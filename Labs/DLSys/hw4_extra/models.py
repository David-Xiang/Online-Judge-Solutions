import sys
sys.path.append('./python')
import needle as ndl
import needle.nn as nn
import math
import numpy as np
np.random.seed(0)


class ConvBN(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride,
        device=None,
        dtype="float32",
    ):
        self.conv = nn.Conv(
            in_channels,
            out_channels,
            kernel_size,
            stride,
            device=device,
            dtype=dtype,
        )
        self.norm = nn.BatchNorm2d(
            out_channels,
            device=device,
            dtype=dtype,
        )
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv(x)
        x = self.norm(x)
        x = self.relu(x)
        return x


class ResNet9(ndl.nn.Module):
    def __init__(self, device=None, dtype="float32"):
        super().__init__()
        self.device = device
        self.dtype = dtype
        self.m = nn.Sequential(
            self.convbn(3, 16, 7, 4),
            self.convbn(16, 32, 3, 2),
            nn.Residual(
                nn.Sequential(self.convbn(32, 32, 3, 1), self.convbn(32, 32, 3, 1))
            ),
            self.convbn(32, 64, 3, 2),
            self.convbn(64, 128, 3, 2),
            nn.Residual(
                nn.Sequential(self.convbn(128, 128, 3, 1), self.convbn(128, 128, 3, 1))
            ),
            nn.Flatten(),
            nn.Linear(128, 128, device=self.device, dtype=self.dtype),
            nn.ReLU(),
            nn.Linear(128, 10, device=self.device, dtype=self.dtype),
        )

    def convbn(self, a, b, k, s):
        return ConvBN(a, b, k, s, device=self.device, dtype=self.dtype)

    def forward(self, x):
        return self.m(x)


class LanguageModel(nn.Module):
    def __init__(self, embedding_size, output_size, hidden_size, num_layers=1,
                 seq_model='rnn', seq_len=40, device=None, dtype="float32"):
        """
        Consists of an embedding layer, a sequence model (either RNN or LSTM), and a
        linear layer.
        Parameters:
        output_size: Size of dictionary
        embedding_size: Size of embeddings
        hidden_size: The number of features in the hidden state of LSTM or RNN
        seq_model: 'rnn' or 'lstm', whether to use RNN or LSTM
        num_layers: Number of layers in RNN or LSTM
        """
        super(LanguageModel, self).__init__()
        self.seq_model = seq_model
        self.output_size = output_size
        if seq_model == "transformer":
            self.embedding = nn.Embedding(
                output_size,
                embedding_size,
                device=device,
                dtype=dtype,
            )
            self.linear = nn.Linear(
                in_features=embedding_size,
                out_features=output_size,
                device=device,
                dtype=dtype,
            )
        else:
            self.embedding = nn.Embedding(
                output_size,
                hidden_size,
                device=device,
                dtype=dtype,
            )
            self.linear = nn.Linear(
                in_features=hidden_size,
                out_features=output_size,
                device=device,
                dtype=dtype,
            )
        if seq_model == "rnn":
            self.seq = nn.RNN(
                hidden_size,
                hidden_size,
                num_layers=num_layers,
                device=device,
                dtype=dtype,
            )
        elif seq_model == "transformer":
            self.seq = nn.Transformer(
                embedding_size=embedding_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                device=device,
                dtype=dtype,
                batch_first=False,
                sequence_len=seq_len,
            )
        else:
            self.seq = nn.LSTM(
                hidden_size,
                hidden_size,
                num_layers=num_layers,
                device=device,
                dtype=dtype,
            )

    def forward(self, x, h=None):
        """
        Given sequence (and the previous hidden state if given), returns probabilities of next word
        (along with the last hidden state from the sequence model).
        Inputs:
        x of shape (seq_len, bs)
        h of shape (num_layers, bs, hidden_size) if using RNN,
            else h is tuple of (h0, c0), each of shape (num_layers, bs, hidden_size)
        Returns (out, h)
        out of shape (seq_len*bs, output_size)
        h of shape (num_layers, bs, hidden_size) if using RNN,
            else h is tuple of (h0, c0), each of shape (num_layers, bs, hidden_size)
        """
        x = self.embedding(x)
        x, h = self.seq(x, h)
        T, B, D = x.shape
        x = x.reshape((T * B, D))
        x = self.linear(x)
        return x, h


if __name__ == "__main__":
    device = ndl.backend_ndarray.cpu()
    model = ResNet9(device=device)
    x = ndl.Tensor(np.random.rand(1, 3, 32, 32), requires_grad=True, device=device)
    model(x)
    cifar10_train_dataset = ndl.data.CIFAR10Dataset(
        "data/cifar-10-batches-py", train=True
    )
    train_loader = ndl.data.DataLoader(cifar10_train_dataset, 128, ndl.cpu())
    print(cifar10_train_dataset[1][0].shape)
