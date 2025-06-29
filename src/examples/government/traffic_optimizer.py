import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def traffic_optimizer(user_logs):
    # Mock movement patterns: {hour: traffic_level}
    mock_data = user_logs or {8: 0.8, 17: 0.9}  # Traffic at 8 AM, 5 PM
    weights = federated_update(mock_data)
    flow = "Optimize" if weights['fc.weight'][0][0] < -70 else "Normal"
    return f"Optimized traffic flow with weights: {weights}\nFlow status: {flow}"

if __name__ == "__main__":
    print(traffic_optimizer(None))