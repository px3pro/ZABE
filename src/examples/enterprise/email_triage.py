import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def email_triage(user_logs):
    # Mock email activity: {hour: email_count}
    mock_data = user_logs or {9: 10, 14: 5}  # Emails at 9 AM, 2 PM
    weights = federated_update(mock_data)
    priority = "High" if weights['fc.weight'][0][0] > -65 else "Low"
    return f"Optimized email triage with weights: {weights}\nPriority: {priority}"

if __name__ == "__main__":
    print(email_triage(None))