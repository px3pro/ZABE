import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from layer1.prophet_predictor import pre_trained_predictor
from layer2.federated_trainer import federated_update
from layer3.contextual_bandit import edge_learn
from examples.healthcare.medication_tracker import track_medication
from examples.finance.budget_assistant import budget_assistant
from examples.smart_home.energy_optimizer import energy_optimizer
from examples.automotive.driver_coach import driver_coach
from examples.retail.recommendation_engine import recommendation_engine
from examples.enterprise.email_triage import email_triage
from examples.government.traffic_optimizer import traffic_optimizer
from examples.education.adaptive_tutor import adaptive_tutor
from examples.media.content_curator import content_curator
from examples.legal.contract_review import contract_review

def orchestrate_zabe():
    # Layer 1: Generic prediction
    print("Layer 1 - Prophet Prediction:")
    predictions = pre_trained_predictor()
    for date, value in zip(predictions['ds'], predictions['yhat']):
        status = "Awake" if value > 0.5 else "Asleep"
        print(f"{date}: {status}")

    # Layer 2: Federated update with mock data
    mock_data = {8: 1, 17: 1}  # Example data
    weights = federated_update(mock_data)
    print("\nLayer 2 - Federated Weights:", weights)

    # Layer 3: Contextual suggestion
    hour = 8
    feedback = "completed"
    suggestion = edge_learn(hour, feedback)
    print("\nLayer 3 - Contextual Suggestion:", suggestion)

    # Run all plugins
    print("\nRunning Plugins:")
    print(track_medication(None))
    print(budget_assistant(None))
    print(energy_optimizer(None))
    print(driver_coach(None))
    print(recommendation_engine(None))
    print(email_triage(None))
    print(traffic_optimizer(None))
    print(adaptive_tutor(None))
    print(content_curator(None))
    print(contract_review(None))

if __name__ == "__main__":
    orchestrate_zabe()