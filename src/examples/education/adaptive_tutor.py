import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update
from src.layer3.contextual_bandit import edge_learn

def adaptive_tutor(user_logs):
    # Mock study logs: {hour: focus_level}
    mock_data = user_logs or {10: 0.7, 15: 0.5}  # Focus at 10 AM, 3 PM
    weights = federated_update(mock_data)
    hour = 10
    feedback = "completed" if mock_data.get(hour, 0) > 0.6 else "skipped"
    suggestion = edge_learn(hour, feedback)
    return f"Optimized tutoring with weights: {weights}\nLesson suggestion: {suggestion}"

if __name__ == "__main__":
    print(adaptive_tutor(None))