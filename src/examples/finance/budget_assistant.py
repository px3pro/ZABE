import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def budget_assistant(user_logs):
    # Mock user logs: {hour: spending_amount}
    mock_data = user_logs or {17: 100, 18: 50}  # Spending at 5 PM, 6 PM
    weights = federated_update(mock_data)
    return f"Optimized budget plan with weights: {weights}"

if __name__ == "__main__":
    print(budget_assistant(None))