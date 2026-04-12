import torch
import torch.nn as nn
from torchtyping import TensorType

class SingleHeadAttention(nn.Module):

    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        # Create three linear projections (Key, Query, Value) with bias=False
        # Instantiation order matters for reproducible weights: key, query, value
        self.W_K = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.W_Q = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.W_V = nn.Linear(embedding_dim, attention_dim, bias=False)

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # 1. Project input through K, Q, V linear layers
        # 2. Compute attention scores: (Q @ K^T) / sqrt(attention_dim)
        # 3. Apply causal mask: use torch.tril(torch.ones(...)) to build lower-triangular matrix,
        #    then masked_fill positions where mask == 0 with float('-inf')
        # 4. Apply softmax(dim=2) to masked scores
        # 5. Return (scores @ V) rounded to 4 decimal places

        
        embedding_dim, attention_dim = self.W_K.in_features, self.W_K.out_features
        assert embedded.shape[2] == embedding_dim
        batch_size, length, embedding_dim = embedded.shape

        # Project input into Key, Query, Value spaces
        K = self.W_K(embedded)
        Q = self.W_Q(embedded)
        V = self.W_V(embedded)
        assert K.shape == Q.shape == V.shape == (batch_size, length, attention_dim)

        assert K.transpose(1, 2).shape == (batch_size, attention_dim, length)
        att = Q @ K.transpose(1, 2) / (attention_dim ** 0.5)
        assert att.shape == (batch_size, length, length)

        att = att.tril()
        att[att == 0] = -torch.inf
        att = torch.softmax(att, axis=2)
        assert att.shape == (batch_size, length, length)
        att = att @ V
        assert att.shape == (batch_size, length, attention_dim)
        return att
