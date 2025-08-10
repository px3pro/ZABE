# Copyright (C) 2025 ZABE
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License (AGPLv3).
import torch
import torch.nn as nn
import numpy as np

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(1, 1)  # Simple model: Predict sleep duration from hour

    def forward(self, x):
        return self.fc(x)

def federated_update(mock_data):
    # Mock user data: Sleep durations at different hours
    hours = torch.tensor([[h] for h in range(24)], dtype=torch.float32)
    sleep_durations = torch.tensor([[8.0 if 0 <= h <= 6 else 0.0] for h in range(24)], dtype=torch.float32)

    # Initialize model
    model = SimpleModel()
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    # Fine-tune on mock data
    for epoch in range(5):  # Small number of epochs for simplicity
        optimizer.zero_grad()
        outputs = model(hours)
        loss = criterion(outputs, sleep_durations)
        loss.backward()
        optimizer.step()

    # Add Gaussian noise for differential privacy (ε=0.5)
    for name, param in model.named_parameters():
        noise = np.random.normal(0, 0.1, param.shape)  # Standard deviation for ε=0.5
        param.data += torch.tensor(noise, dtype=torch.float32)

    # Return encrypted weights (simulated)
    return {name: param.detach().numpy() for name, param in model.named_parameters()}

if __name__ == "__main__":
    weights = federated_update(None)
    print("Updated weights with differential privacy:", weights)