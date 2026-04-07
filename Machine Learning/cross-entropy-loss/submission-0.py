import numpy as np
from numpy.typing import NDArray
import torch

class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        eps = 1e-7
        y_true = torch.from_numpy(y_true)
        y_pred = torch.from_numpy(y_pred + eps)
        loss = y_true * torch.log(y_pred)
        loss += (1 - y_true) * torch.log(1 - y_pred)
        loss = -1.0 / len(y_true) * loss.sum()
        return loss.numpy().round(4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        y_true = torch.from_numpy(y_true)
        y_pred = torch.from_numpy(y_pred)

        return (-1.0 / len(y_true) * (y_true * torch.log(y_pred)).sum()).numpy().round(4)
