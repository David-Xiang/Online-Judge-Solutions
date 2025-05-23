"""hw1/apps/simple_ml.py"""

import struct
import gzip
import numpy as np

import sys

sys.path.append(".")
sys.path.append("python/")
# sys.path.append("apps")
import needle as ndl

import needle.nn as nn
from apps.models import *
import time
device = ndl.cpu()

def parse_mnist(image_filesname, label_filename):
    """Read an images and labels file in MNIST format.  See this page:
    http://yann.lecun.com/exdb/mnist/ for a description of the file format.

    Args:
        image_filename (str): name of gzipped images file in MNIST format
        label_filename (str): name of gzipped labels file in MNIST format

    Returns:
        Tuple (X,y):
            X (numpy.ndarray[np.float32]): 2D numpy array containing the loaded
                data.  The dimensionality of the data should be
                (num_examples x input_dim) where 'input_dim' is the full
                dimension of the data, e.g., since MNIST images are 28x28, it
                will be 784.  Values should be of type np.float32, and the data
                should be normalized to have a minimum value of 0.0 and a
                maximum value of 1.0.

            y (numpy.ndarray[dypte=np.int8]): 1D numpy array containing the
                labels of the examples.  Values should be of type np.int8 and
                for MNIST will contain the values 0-9.
    """
    ### BEGIN YOUR SOLUTION
    raise NotImplementedError()
    ### END YOUR SOLUTION


def softmax_loss(Z, y_one_hot):
    """Return softmax loss.  Note that for the purposes of this assignment,
    you don't need to worry about "nicely" scaling the numerical properties
    of the log-sum-exp computation, but can just compute this directly.

    Args:
        Z (ndl.Tensor[np.float32]): 2D Tensor of shape
            (batch_size, num_classes), containing the logit predictions for
            each class.
        y (ndl.Tensor[np.int8]): 2D Tensor of shape (batch_size, num_classes)
            containing a 1 at the index of the true label of each example and
            zeros elsewhere.

    Returns:
        Average softmax loss over the sample. (ndl.Tensor[np.float32])
    """
    ### BEGIN YOUR SOLUTION
    raise NotImplementedError()
    ### END YOUR SOLUTION


def nn_epoch(X, y, W1, W2, lr=0.1, batch=100):
    """Run a single epoch of SGD for a two-layer neural network defined by the
    weights W1 and W2 (with no bias terms):
        logits = ReLU(X * W1) * W1
    The function should use the step size lr, and the specified batch size (and
    again, without randomizing the order of X).

    Args:
        X (np.ndarray[np.float32]): 2D input array of size
            (num_examples x input_dim).
        y (np.ndarray[np.uint8]): 1D class label array of size (num_examples,)
        W1 (ndl.Tensor[np.float32]): 2D array of first layer weights, of shape
            (input_dim, hidden_dim)
        W2 (ndl.Tensor[np.float32]): 2D array of second layer weights, of shape
            (hidden_dim, num_classes)
        lr (float): step size (learning rate) for SGD
        batch (int): size of SGD mini-batch

    Returns:
        Tuple: (W1, W2)
            W1: ndl.Tensor[np.float32]
            W2: ndl.Tensor[np.float32]
    """

    ### BEGIN YOUR SOLUTION
    raise NotImplementedError()
    ### END YOUR SOLUTION

### CIFAR-10 training ###
def epoch_general_cifar10(dataloader, model, loss_fn=nn.SoftmaxLoss(), opt=None):
    """
    Iterates over the dataloader. If optimizer is not None, sets the
    model to train mode, and for each batch updates the model parameters.
    If optimizer is None, sets the model to eval mode, and simply computes
    the loss/accuracy.

    Args:
        dataloader: Dataloader instance
        model: nn.Module instance
        loss_fn: nn.Module instance
        opt: Optimizer instance (optional)

    Returns:
        avg_acc: average accuracy over dataset
        avg_loss: average loss over dataset
    """
    np.random.seed(4)
    if opt:
        model.train()
    else:
        model.eval()

    loss_sum = 0
    err_count = 0
    sample_count = 0
    device = model.device
    for i, batch in enumerate(dataloader):
        X, y = batch
        X, y = ndl.Tensor(X, device=device), ndl.Tensor(y, device=device)
        y_pred = model.forward(X)
        loss = loss_fn(y_pred, y)
        err_count += np.sum(y_pred.numpy().argmax(axis=1) != y.numpy())
        loss_sum += loss.numpy() * X.shape[0]
        sample_count += X.shape[0]
        if opt:
            opt.reset_grad()
            loss.backward()
            opt.step()
    return 1 - (err_count / sample_count), loss_sum / sample_count

def train_cifar10(model, dataloader, n_epochs=1, optimizer=ndl.optim.Adam,
          lr=0.001, weight_decay=0.001, loss_fn=nn.SoftmaxLoss):
    """
    Performs {n_epochs} epochs of training.

    Args:
        dataloader: Dataloader instance
        model: nn.Module instance
        n_epochs: number of epochs (int)
        optimizer: Optimizer class
        lr: learning rate (float)
        weight_decay: weight decay (float)
        loss_fn: nn.Module class

    Returns:
        avg_acc: average accuracy over dataset from last epoch of training
        avg_loss: average loss over dataset from last epoch of training
    """
    np.random.seed(4)
    opt = optimizer(model.parameters(), lr=lr, weight_decay=weight_decay)
    acc, loss = 0, 0
    for e in range(n_epochs):
        st = time.time()
        acc, loss = epoch_general_cifar10(dataloader, model, loss_fn=loss_fn(), opt=opt)
        print(f"epoch {e}: {acc=:.4f} {loss[0]=:.4f}, use {time.time() - st:.2f} s")
    return acc, loss


def evaluate_cifar10(model, dataloader, loss_fn=nn.SoftmaxLoss):
    """
    Computes the test accuracy and loss of the model.

    Args:
        dataloader: Dataloader instance
        model: nn.Module instance
        loss_fn: nn.Module class

    Returns:
        avg_acc: average accuracy over dataset
        avg_loss: average loss over dataset
    """
    np.random.seed(4)
    st = time.time()
    acc, loss = epoch_general_cifar10(dataloader, model, loss_fn=loss_fn(), opt=None)
    print(f"eval: {acc=:.4f} {loss[0]=:.4f}, use {time.time() - st:.2f} s")
    return acc, loss


### PTB training ###
def epoch_general_ptb(data, model, seq_len=40, loss_fn=nn.SoftmaxLoss(), opt=None,
        clip=None, device=None, dtype="float32"):
    """
    Iterates over the data. If optimizer is not None, sets the
    model to train mode, and for each batch updates the model parameters.
    If optimizer is None, sets the model to eval mode, and simply computes
    the loss/accuracy.

    Args:
        data: data of shape (nbatch, batch_size) given from batchify function
        model: LanguageModel instance
        seq_len: i.e. bptt, sequence length
        loss_fn: nn.Module instance
        opt: Optimizer instance (optional)
        clip: max norm of gradients (optional)

    Returns:
        avg_acc: average accuracy over dataset
        avg_loss: average loss over dataset
    """
    np.random.seed(4)
    if opt:
        model.train()
    else:
        model.eval()

    loss_sum = 0
    err_count = 0
    sample_count = 0
    batches = data.shape[0] // seq_len
    print(f"{batches=}")
    for i in range(batches):
        if i % 100 == 0:
            print(f"{i=}")
        X, y = ndl.data.datasets.ptb_dataset.get_batch(
            data, i, seq_len, device=device, dtype=dtype
        )
        y_pred, h = model.forward(X)
        loss = loss_fn(y_pred, y)
        err_count += np.sum(y_pred.numpy().argmax(axis=1) != y.numpy())
        loss_sum += loss.numpy() * X.shape[0]
        sample_count += X.shape[0]
        if opt:
            opt.reset_grad()
            loss.backward()
            if clip:
                opt.clip_grad_norm(clip)
            opt.step()
        if i == 5000:
            break
    return 1 - (err_count / sample_count), loss_sum / sample_count

def train_ptb(model, data, seq_len=40, n_epochs=1, optimizer=ndl.optim.SGD,
          lr=4.0, weight_decay=0.0, loss_fn=nn.SoftmaxLoss, clip=None,
          device=None, dtype="float32"):
    """
    Performs {n_epochs} epochs of training.

    Args:
        model: LanguageModel instance
        data: data of shape (nbatch, batch_size) given from batchify function
        seq_len: i.e. bptt, sequence length
        n_epochs: number of epochs (int)
        optimizer: Optimizer class
        lr: learning rate (float)
        weight_decay: weight decay (float)
        loss_fn: nn.Module class
        clip: max norm of gradients (optional)

    Returns:
        avg_acc: average accuracy over dataset from last epoch of training
        avg_loss: average loss over dataset from last epoch of training
    """
    np.random.seed(4)
    opt = optimizer(model.parameters(), lr=lr, weight_decay=weight_decay)
    acc, loss = 0, 0
    for e in range(n_epochs):
        st = time.time()
        acc, loss = epoch_general_ptb(
            data,
            model,
            seq_len=seq_len,
            loss_fn=loss_fn(),
            opt=opt,
            clip=clip,
            device=device,
            dtype=dtype,
        )
        print(f"epoch {e}: {acc=:.4f} {loss[0]=:.4f}, use {time.time() - st:.2f} s")
    return acc, loss


def evaluate_ptb(model, data, seq_len=40, loss_fn=nn.SoftmaxLoss,
        device=None, dtype="float32"):
    """
    Computes the test accuracy and loss of the model.

    Args:
        model: LanguageModel instance
        data: data of shape (nbatch, batch_size) given from batchify function
        seq_len: i.e. bptt, sequence length
        loss_fn: nn.Module class

    Returns:
        avg_acc: average accuracy over dataset
        avg_loss: average loss over dataset
    """
    np.random.seed(4)
    st = time.time()
    acc, loss = epoch_general_ptb(
        data,
        model,
        seq_len=seq_len,
        loss_fn=loss_fn(),
        device=device,
        dtype=dtype,
    )
    print(f"eval: {acc=:.4f} {loss[0]=:.4f}, use {time.time() - st:.2f} s")
    return acc, loss


### CODE BELOW IS FOR ILLUSTRATION, YOU DO NOT NEED TO EDIT


def loss_err(h, y):
    """Helper function to compute both loss and error"""
    y_one_hot = np.zeros((y.shape[0], h.shape[-1]))
    y_one_hot[np.arange(y.size), y] = 1
    y_ = ndl.Tensor(y_one_hot)
    return softmax_loss(h, y_).numpy(), np.mean(h.numpy().argmax(axis=1) != y)


def resnet_e2e():
    device = ndl.cpu()
    print(f"{device=}")
    train_dataset = ndl.data.CIFAR10Dataset("data/cifar-10-batches-py", train=True)
    train_dataloader = ndl.data.DataLoader(
        dataset=train_dataset,
        batch_size=128,
        shuffle=True,
    )
    model = ResNet9(device=device, dtype="float32")
    train_cifar10(
        model,
        train_dataloader,
        n_epochs=10,
        optimizer=ndl.optim.Adam,
        lr=0.001,
        weight_decay=0.001,
    )
    test_dataset = ndl.data.CIFAR10Dataset("data/cifar-10-batches-py", train=False)
    test_dataloader = ndl.data.DataLoader(
        dataset=train_dataset,
        batch_size=128,
        shuffle=True,
    )
    evaluate_cifar10(model, test_dataloader)


def language_model_e2e():
    device = ndl.cpu()
    print(f"{device=}")
    corpus = ndl.data.Corpus("data/ptb")
    train_data = ndl.data.batchify(
        corpus.train, batch_size=16, device=device, dtype="float32"
    )
    model = LanguageModel(
        30,
        len(corpus.dictionary),
        hidden_size=10,
        num_layers=2,
        seq_model="rnn",
        device=device,
    )
    train_ptb(model, train_data, seq_len=1, n_epochs=1, device=device)
    test_data = ndl.data.batchify(
        corpus.test, batch_size=16, device=device, dtype="float32"
    )
    evaluate_ptb(model, test_data, seq_len=40, device=device)
