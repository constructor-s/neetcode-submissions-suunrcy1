import numpy as np
from numpy.typing import NDArray
import torch


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        return torch.round(
            1.0 / (1 + torch.exp(-torch.as_tensor(z)))
            , decimals=5
        ).numpy()

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        return torch.relu(torch.as_tensor(z)).numpy()
