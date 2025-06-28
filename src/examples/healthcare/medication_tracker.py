import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update
from src.layer3.contextual_bandit import edge_learn

def track_medication(user_logs):
    # Mock wearables data: {hour: [ECG_value, glucose_level]}
    mock_data = user_logs or {8: [70, 90], 20: [65, 85]}  # ECG, glucose at 8 AM, 8 PM
    weights = federated_update(mock_data)
    # Use contextual bandit for therapy suggestion
    hour = 8
    feedback = "completed" if mock_data.get(hour, [0, 0])[0] > 60 else "skipped"
    suggestion = edge_learn(hour, feedback)
    return f"Optimized medication schedule with weights: {weights}\nTherapy suggestion: {suggestion}"

if __name__ == "__main__":
    print(track_medication(None))