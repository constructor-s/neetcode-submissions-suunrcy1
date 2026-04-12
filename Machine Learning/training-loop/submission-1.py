import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def train(self, X: NDArray[np.float64], y: NDArray[np.float64], epochs: int, lr: float) -> Tuple[NDArray[np.float64], float]:
        # X: (n_samples, n_features)
        # y: (n_samples,) targets
        # epochs: number of training iterations
        # lr: learning rate
        #
        # Model: y_hat = X @ w + b
        # Loss: MSE = (1/n) * sum((y_hat - y)^2)
        # Initialize w = zeros, b = 0
        # return (np.round(w, 5), round(b, 5))
        n, n_feat = X.shape
        y = y.reshape(n, 1)

        w = np.zeros([n_feat, 1], dtype=np.float32)
        b = 0

        n = len(X)
        for _ in range(epochs):
            # Forward
            y_ = (X @ w) + b
            assert y_.shape == (n, 1)
            
            # Back
            dL_dy_ = 2.0 / n * (y_ - y)
            assert dL_dy_.shape == (n, 1)
            # assert (dL_dy_ * X).sum(0, keepdims=True).shape == (1, n_feat)
            w -= lr * (X.T @ dL_dy_)
            b -= lr * dL_dy_.sum() 
            
        return (
            w.ravel().round(5),
            round(b, 5)
        )
