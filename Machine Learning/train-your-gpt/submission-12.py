import torch
import torch.nn as nn
import torch.nn.functional as F

# The GPT model is provided for you. It returns raw logits (not probabilities).
# You only need to implement the training loop below.

class Solution:
    def train(self, model: nn.Module, data: torch.Tensor, epochs: int, context_length: int, batch_size: int, lr: float) -> float:
        # Train the GPT model and return the final loss (rounded to 4 decimals).
        #
        # Steps:
        # 1. Create an AdamW optimizer with the given learning rate
        # 2. For each epoch:
        #    a. Use torch.manual_seed(epoch) for reproducibility
        #    b. Sample random start indices with torch.randint
        #    c. Build X (input) and Y (target) batches, each (batch_size, context_length)
        #       Y is X shifted right by 1
        #    d. Forward pass: logits = model(X), shape (batch_size, context_length, vocab_size)
        #    e. Reshape for cross_entropy: logits to (B*T, C), targets to (B*T)
        #    f. Compute loss = F.cross_entropy(logits_flat, targets_flat)
        #    g. optimizer.zero_grad(), loss.backward(), optimizer.step()
        # 3. Return the final loss value rounded to 4 decimals
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        for epoch in range(epochs):
            torch.manual_seed(epoch)
            start_indices = torch.randint(0, len(data) - context_length, (batch_size,))

            X = torch.stack([data[s:s+context_length] for s in start_indices])
            Y = torch.stack([data[s+1:s+context_length+1] for s in start_indices])
            assert X.shape == (batch_size, context_length)
            assert Y.shape == (batch_size, context_length)
            
            logits = model(X)
            assert logits.shape[:2] == (batch_size, context_length)
            vocab_size = logits.shape[2]            
            
            loss = F.cross_entropy(
                logits.view(batch_size * context_length, vocab_size),
                Y.view(batch_size * context_length)
            )

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        return round(loss.item(), 4)
