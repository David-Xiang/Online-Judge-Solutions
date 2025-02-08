"""hw1/apps/simple_ml.py"""

import struct
import gzip
import numpy as np

import sys

sys.path.append("python/")
import needle as ndl


def parse_images(bytes):
    magic, num_images, rows, cols = struct.unpack_from(">4i", bytes, offset=0)
    assert magic == 2051
    assert rows == 28
    assert cols == 28

    offset = 16
    images = np.ndarray((num_images, 784), np.float32)
    for i in range(num_images):
        pixels = struct.unpack_from(">784B", bytes, offset=offset)
        for j in range(784):
            pixel = pixels[j]
            assert 0 <= pixel <= 255
            images[i][j] = pixels[j] / 255.0
        offset = offset + 784
    return images


def parse_labels(bytes):
    magic, num_labels = struct.unpack_from(">2i", bytes, offset=0)
    assert magic == 2049

    offset = 8
    labels = np.ndarray((num_labels), np.uint8)
    for i in range(num_labels):
        (label,) = struct.unpack_from(">B", bytes, offset=offset)
        offset = offset + 1
        assert 0 <= label <= 9
        labels[i] = label
    return labels


def parse_mnist(image_filename, label_filename):
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
    with gzip.open(image_filename) as image_file:
        X = parse_images(image_file.read())
    with gzip.open(label_filename) as label_file:
        y = parse_labels(label_file.read())
    return X, y


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
    batch_size = ndl.summation(y_one_hot) # (1,)
    pred_sum = ndl.log(ndl.summation(ndl.exp(Z), axes=(1,))) # (batch_size,)
    label_sum = ndl.summation(Z * y_one_hot, axes=(1,)) # (batch_size,)
    losses = ndl.add(pred_sum, ndl.negate(label_sum)) # (batch_size,)
    loss_sum = ndl.summation(losses) # (1,)
    return ndl.divide(loss_sum, batch_size)


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
    num_examples = X.shape[0]
    num_classes = W2.shape[1]
    batches = int(np.ceil(num_examples * 1.0 / batch))
    for i in range(batches):
        X_b = ndl.Tensor(X[i * batch : (i + 1) * batch,])
        y_b = y[i * batch : (i + 1) * batch]
        I_b = ndl.Tensor(np.eye(num_classes)[y_b])
        pred = ndl.relu(X_b @ W1) @ W2
        loss = softmax_loss(pred, I_b)
        loss.backward()
        W1_weight = W1.data - lr * W1.grad.data # numpy computations
        W2_weight = W2.data - lr * W2.grad.data # numpy computations
        W1 = ndl.Tensor(W1_weight)
        W2 = ndl.Tensor(W2_weight)
    return W1, W2


### CODE BELOW IS FOR ILLUSTRATION, YOU DO NOT NEED TO EDIT


def loss_err(h, y):
    """Helper function to compute both loss and error"""
    y_one_hot = np.zeros((y.shape[0], h.shape[-1]))
    y_one_hot[np.arange(y.size), y] = 1
    y_ = ndl.Tensor(y_one_hot)
    return softmax_loss(h, y_).numpy(), np.mean(h.numpy().argmax(axis=1) != y)
