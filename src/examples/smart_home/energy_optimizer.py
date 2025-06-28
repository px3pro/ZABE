import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def energy_optimizer(user_logs):
    # Mock user logs: {hour: occupancy_level}
    mock_data = user_logs or {8: 1, 20: 1}  # Occupied at 8 AM, 8 PM
    weights = federated_update(mock_data)
    return f"Optimized energy schedule with weights: {weights}"

if __name__ == "__main__":
    print(energy_optimizer(None))