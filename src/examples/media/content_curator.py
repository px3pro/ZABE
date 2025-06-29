import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.layer2.federated_trainer import federated_update

def content_curator(user_logs):
    # Mock viewing logs: {hour: watch_time}
    mock_data = user_logs or {19: 60, 21: 30}  # Watch time at 7 PM, 9 PM
    weights = federated_update(mock_data)
    rec = "Movie" if weights['fc.weight'][0][0] > -65 else "TV Show"
    return f"Optimized content curation with weights: {weights}\nRecommendation: {rec}"

if __name__ == "__main__":
    print(content_curator(None))