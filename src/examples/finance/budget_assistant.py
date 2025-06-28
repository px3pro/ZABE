import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def budget_assistant(user_logs):
    # Mock spending logs: {hour: spending_amount}
    mock_data = user_logs or {17: 100, 18: 50}  # Spending at 5 PM, 6 PM
    weights = federated_update(mock_data)
    # Fraud detection flag
    fraud_flag = "Possible fraud" if any(v > 75 for v in mock_data.values()) else "Safe"
    return f"Optimized budget plan with weights: {weights}\nFraud status: {fraud_flag}"

if __name__ == "__main__":
    print(budget_assistant(None))