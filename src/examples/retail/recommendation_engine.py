import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def recommendation_engine(user_logs):
    # Mock purchase logs: {hour: purchase_amount}
    mock_data = user_logs or {10: 50, 15: 30}  # Purchases at 10 AM, 3 PM
    weights = federated_update(mock_data)
    # Private recommendation
    rec = "Suggested item: Book" if weights['fc.weight'][0][0] > -65 else "Suggested item: Electronics"
    return f"Optimized recommendation with weights: {weights}\n{rec}"

if __name__ == "__main__":
    print(recommendation_engine(None))