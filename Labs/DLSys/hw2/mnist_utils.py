import gzip
import struct
import numpy as np


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
    with gzip.open(image_filename) as image_file:
        X = parse_images(image_file.read())
    with gzip.open(label_filename) as label_file:
        y = parse_labels(label_file.read())
    return X, y

