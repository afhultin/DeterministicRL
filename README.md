# Reinforcement Learning Algorithms

Three classic reinforcement learning algorithms implemented in Python on a 3x4 gridworld environment with terminal states and varying reward values.

## Algorithms

### Value Iteration (`valueIteration.py`)
Iteratively computes the optimal value function by applying the Bellman optimality equation until convergence, then extracts the greedy policy.

### Policy Iteration (`PolicyIteration.py`)
Alternates between policy evaluation (computing V for a fixed policy) and policy improvement (making the policy greedy with respect to V) until the policy stabilizes.

### Q-Learning (`qLearning.py`)
Builds a Q-table mapping state-action pairs to expected returns using the Bellman equation, then derives the optimal policy from the converged Q-values.

## Environment

A 3x4 grid with 4 terminal states carrying rewards of -20, -10, +10, and +20. The agent can move Up, Down, Left, or Right. Moving off the grid results in staying in place.

Each algorithm runs with three discount factors (gamma = 0.9, 0.5, 0.1) to demonstrate how discounting affects the learned policy.

## Usage

```bash
python valueIteration.py
python PolicyIteration.py
python qLearning.py
```

Each script prints the number of iterations to convergence, the derived policy, and value estimates for key states.

Built for an Artificial Intelligence course.
