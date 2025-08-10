# Copyright (C) 2025 ZABE
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License (AGPLv3).
import numpy as np

class ContextualBandit:
    def __init__(self, n_arms=2, context_dim=1):
        self.n_arms = n_arms  # Actions: e.g., suggest "Drink water" or "Skip"
        self.context_dim = context_dim  # Context: e.g., hour of day
        self.weights = np.zeros((n_arms, context_dim))  # Initialize weights
        self.n = np.zeros(n_arms)  # Counts
        self.v = np.zeros(n_arms)  # Values

    def select_arm(self, context):
        scores = np.dot(self.weights, context)
        return np.argmax(scores + np.sqrt(2 * np.log(sum(self.n) + 1) / (self.n + 1e-6)))

    def update(self, context, arm, reward):
        self.n[arm] += 1
        self.v[arm] += reward
        self.weights[arm] += context * (reward - self.v[arm] / self.n[arm])

def edge_learn(hour, feedback):
    # Persistent bandit instance for testing
    global bandit
    try:
        bandit
    except NameError:
        bandit = ContextualBandit(n_arms=2, context_dim=1)
    context = np.array([hour], dtype=np.float64)
    arm = bandit.select_arm(context)
    reward = 1.0 if feedback == "completed" else -0.5
    bandit.update(context, arm, reward)
    return "Drink water" if arm == 0 else "Skip"

if __name__ == "__main__":
    print(edge_learn(hour=8, feedback="completed"))
    print(edge_learn(hour=8, feedback="skipped"))