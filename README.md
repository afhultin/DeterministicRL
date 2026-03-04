# Reinforcement Learning Algorithms

Three RL algorithms on a 3x4 gridworld: Value Iteration, Policy Iteration, and Q-Learning.

The grid has 4 terminal states with rewards ranging from -20 to +20. Each algorithm runs with three different discount factors (0.9, 0.5, 0.1) to show how gamma affects the learned policy.

## Files

- `valueIteration.py` - computes optimal values via Bellman updates, then extracts the policy
- `PolicyIteration.py` - alternates between evaluating a policy and improving it until stable
- `qLearning.py` - learns Q-values for each state-action pair, derives policy from the table
