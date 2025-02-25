from typing import List, Optional
from ..data_basic import Dataset
import numpy as np
from .mnist_utils import parse_mnist


class MNISTDataset(Dataset):
    def __init__(
        self,
        image_filename: str,
        label_filename: str,
        transforms: Optional[List] = None,
    ):
        self.X, self.y = parse_mnist(image_filename, label_filename)
        self.transforms = transforms

    def __getitem__(self, index) -> object:
        if isinstance(index, int):
            s = slice(index, index+1)
        else:
            s = index
        image = self.X[s, :]
        image = image.reshape(-1, 28, 28, 1)
        for i in range(image.shape[0]):
            image[i,:,:,:] = self.apply_transforms(image[i,:,:,:])
        label = self.y[index]
        return (image, label)

    def __len__(self) -> int:
        return self.X.shape[0]
