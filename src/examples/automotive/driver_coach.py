import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update
from src.layer3.contextual_bandit import edge_learn

def driver_coach(user_logs):
    # Mock driving data: {hour: [speed, braking_force]}
    mock_data = user_logs or {8: [60, 0.5], 17: [80, 0.8]}  # Speed (km/h), braking force
    weights = federated_update(mock_data)
    # Use contextual bandit for coaching
    hour = 8
    feedback = "completed" if mock_data.get(hour, [0, 0])[1] < 0.7 else "skipped"
    suggestion = edge_learn(hour, feedback)
    return f"Optimized driver coaching with weights: {weights}\nCoaching tip: {suggestion}"

if __name__ == "__main__":
    print(driver_coach(None))