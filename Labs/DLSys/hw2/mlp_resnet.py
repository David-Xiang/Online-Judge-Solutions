import sys

sys.path.append("../python")
import needle as ndl
import needle.nn as nn
import numpy as np
import time
import os

np.random.seed(0)
# MY_DEVICE = ndl.backend_selection.cuda()


def ResidualBlock(dim, hidden_dim, norm=nn.BatchNorm1d, drop_prob=0.1):
    res_func = nn.Sequential(
        nn.Linear(in_features=dim, out_features=hidden_dim),
        norm(dim=hidden_dim),
        nn.ReLU(),
        nn.Dropout(p=drop_prob),
        nn.Linear(in_features=hidden_dim, out_features=dim),
        norm(dim=dim),
    )
    return nn.Sequential(
        nn.Residual(res_func),
        nn.ReLU(),
    )


def MLPResNet(
    dim,
    hidden_dim=100,
    num_blocks=3,
    num_classes=10,
    norm=nn.BatchNorm1d,
    drop_prob=0.1,
):
    blocks = [
        nn.Flatten(),
        nn.Linear(in_features=dim, out_features=hidden_dim),
        nn.ReLU(),
    ]
    for i in range(num_blocks):
        blocks.append(
            ResidualBlock(
                dim=hidden_dim,
                hidden_dim=hidden_dim // 2,
                norm=norm,
                drop_prob=drop_prob,
            )
        )
    blocks.append(nn.Linear(in_features=hidden_dim, out_features=num_classes))
    return nn.Sequential(*blocks)


def epoch(dataloader, model, opt=None):
    np.random.seed(4)
    if opt:
        model.train()
    else:
        model.eval()

    loss_func = nn.SoftmaxLoss()
    loss_sum = 0
    err_count = 0
    sample_count = 0
    for i, batch in enumerate(dataloader):
        X, y = batch
        y_pred = model.forward(X)
        loss = loss_func(y_pred, y)
        err_count += np.sum(y_pred.numpy().argmax(axis=1) != y.numpy())
        loss_sum += loss.numpy() * X.shape[0]
        sample_count += X.shape[0]
        if opt:
            opt.reset_grad()
            loss.backward()
            opt.step()
    return err_count / sample_count, loss_sum / sample_count


def train_mnist(
    batch_size=100,
    epochs=10,
    optimizer=ndl.optim.Adam,
    lr=0.001,
    weight_decay=0.001,
    hidden_dim=100,
    data_dir="data",
):
    np.random.seed(4)
    train_set = ndl.data.MNISTDataset(
        f"{data_dir}/train-images-idx3-ubyte.gz",
        f"{data_dir}/train-labels-idx1-ubyte.gz",
    )
    test_set = ndl.data.MNISTDataset(
        f"{data_dir}/t10k-images-idx3-ubyte.gz",
        f"{data_dir}/t10k-labels-idx1-ubyte.gz",
    )
    train_data_loader = ndl.data.DataLoader(
        train_set, batch_size=batch_size, shuffle=True
    )
    test_data_loader = ndl.data.DataLoader(test_set, batch_size=batch_size)

    model = MLPResNet(784, hidden_dim=hidden_dim)
    opt = optimizer(model.parameters(), lr=lr, weight_decay=weight_decay)
    train_loss, train_err, test_loss, test_error = 0, 0, 0, 0
    for e in range(epochs):
        train_err, train_loss = epoch(train_data_loader, model, opt=opt)
        test_err, test_loss = epoch(test_data_loader, model, opt=None)
    return train_err, train_loss, test_err, test_loss


if __name__ == "__main__":
    train_mnist(data_dir="../data")
