import numpy as np
from numpy.typing import NDArray
import torch

class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        z = torch.as_tensor(z)
        z = z - torch.max(z)
        z = torch.exp(z)
        z = z / torch.sum(z)
        return z.numpy().round(4)
