# reinforcement-learning
This repository will give deep insights into reinforcement learning. This file consists of various environments and their description.
There are mainly 2 types of problems in RL-
1. model-based RL - In this type, the environment is fully observable or MDP is known for the environment(current state fully describes the environment).
2. model-free RL - In this type, MDP is unknown for the environment.

 Before referring main project its suggested to refer other en




# **Graphs**
##1. Monte Carlo:
![minigrid_mc](https://github.com/user-attachments/assets/e944dae1-7537-426d-a573-447919f90fef)
##2. Sarsa:
![minigrid_sarsa](https://github.com/user-attachments/assets/d2d0fe28-d49d-4672-8d41-c74ef00bfec7)
##3. Sarsa(λ):
![minigrid_sarsa_lambda](https://github.com/user-attachments/assets/c84800a8-87e4-47b5-b5a9-dc3451231ac5)
##4. Q-learning:
![minigrid_q_learning](https://github.com/user-attachments/assets/a7a8c447-2b65-437f-a3d3-98c1d874552d)


 Note-From graphs, we can observe Q-learning algorithm takes more steps to converge than the sarsa(λ) algorithm if hyperparameters are kept the same, the reason is that it explores the environment more than the sarsa(λ) which always takes greedy actions i.e. always exploits the greedy policy.

