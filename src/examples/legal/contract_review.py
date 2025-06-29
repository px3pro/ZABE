import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def contract_review(user_logs):
    # Mock clause logs: {hour: clause_complexity}
    mock_data = user_logs or {10: 0.6, 14: 0.8}  # Complexity at 10 AM, 2 PM
    weights = federated_update(mock_data)
    flag = "Review needed" if weights['fc.weight'][0][0] < -70 else "Safe"
    return f"Optimized contract review with weights: {weights}\nFlag: {flag}"

if __name__ == "__main__":
    print(contract_review(None))