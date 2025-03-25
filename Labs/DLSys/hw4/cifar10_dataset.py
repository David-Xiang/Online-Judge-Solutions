import os
import pickle
from typing import Iterator, Optional, List, Sized, Union, Iterable, Any
import numpy as np
from ..data_basic import Dataset

class CIFAR10Dataset(Dataset):
    def __init__(
        self,
        base_folder: str,
        train: bool,
        p: Optional[int] = 0.5,
        transforms: Optional[List] = None
    ):
        """
        Parameters:
        base_folder - cifar-10-batches-py folder filepath
        train - bool, if True load training dataset, else load test dataset
        Divide pixel values by 255. so that images are in 0-1 range.
        Attributes:
        X - numpy array of images
        y - numpy array of labels
        """
        if train:
            files = [f"{base_folder}/data_batch_{i}" for i in range(1, 6)]
        else:
            files = [f"{base_folder}/test_batch"]
        data_list = []
        self.labels = []
        for f in files:
            with open(f, "rb") as fo:
                dict = pickle.load(fo, encoding="bytes")
                data_list.append(dict[b"data"])
                self.labels.extend(dict[b"labels"])
        self.data = (
            np.stack(data_list)
            .reshape((-1, 3, 32, 32))
            .astype(np.float32)
            .__truediv__(255.0)
        )
        self.labels = np.array(self.labels)
        assert self.data.shape[0] == self.labels.shape[0]

    def __getitem__(self, index) -> object:
        """
        Returns the image, label at given index
        Image should be of shape (3, 32, 32)
        """
        return self.data[index], self.labels[index]

    def __len__(self) -> int:
        """
        Returns the total number of examples in the dataset
        """
        return len(self.labels)
