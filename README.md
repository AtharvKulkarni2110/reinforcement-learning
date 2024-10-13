# reinforcement-learning
This repository will give deep insights into reinforcement learning. This file consists of various environments and their description.
There are mainly 2 types of problems in RL-
1. model-based RL - In this type, the environment is fully observable or MDP is known for the environment(current state fully describes the environment).
2. model-free RL - In this type, MDP is unknown for the environment.
The primary goal is to explore dynamic programming and model-free control algorithms in these environments and analyze their performance.


### Task 1: Frozen Lake Environment using Dynamic Programming

- **Algorithms**:
  - Policy Iteration
  - Value Iteration
- **Environment Documentation**: [Frozen Lake Environment](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)
 
 frozen lake environment-

 
![valueiteration-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/f7d267dc-32ac-4379-aead-29664cef9c5d)




** 1)Observation Space-**

 Consider a 4x4 map, then env.observation_space=discrete(16)
 here each state represents a whole number till 15.
 Further custom maps can be defined and each state can be labeled as either S (start) or 
 F(Frozen), H(Hole) or G(Goal).
 By default mapping, S is at 0 and G is at 15.

2)Action space -
|          |            |        
|----------|------------|
|    0     | Move left  | 
|    1     | Move down  |
|    2     | Move right | 
|    3     | Move up    |


minigrid environment-



![minigrid](https://github.com/user-attachments/assets/6bfc354c-2b17-4dd7-8919-39b1dbe59303)

 



# **Graphs**
##1. Monte Carlo:
![minigrid_mc](https://github.com/user-attachments/assets/e944dae1-7537-426d-a573-447919f90fef)
##2. Sarsa:
![minigrid_sarsa](https://github.com/user-attachments/assets/d2d0fe28-d49d-4672-8d41-c74ef00bfec7)
##3. Sarsa(λ):
![minigrid_sarsa_lambda](https://github.com/user-attachments/assets/c84800a8-87e4-47b5-b5a9-dc3451231ac5)
##4. Q-learning:
![minigrid_q_learning](https://github.com/user-attachments/assets/a7a8c447-2b65-437f-a3d3-98c1d874552d)




