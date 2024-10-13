# reinforcement-learning
This repository will give deep insights into reinforcement learning. This file consists of various environments and their description.
There are mainly 2 types of problems in RL-
1. model-based RL - In this type, the environment is fully observable or MDP is known for the environment(current state fully describes the environment).
2. model-free RL - In this type, MDP is unknown for the environment.
The primary goal is to explore dynamic programming and model-free control algorithms in these environments and analyze their performance.


###  Frozen Lake Environment using Dynamic Programming

- **Algorithms**:
  - Policy Iteration
  - Value Iteration
- **Environment Documentation**: [Frozen Lake Environment](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)
 
 frozen lake environment-

 
![valueiteration-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/f7d267dc-32ac-4379-aead-29664cef9c5d)




1)Observation Space-

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


3)Rewards-
|   |               |
|---|---------------|
| 1 | reaching goal | 
| 0 | otherwise     | 


###  Model-Free Control Algorithms in MiniGrid Empty Space

- **Algorithms**:
  - Monte Carlo
  - Sarsa
  - Sarsa(λ)
  - Q-Learning

- **Environment Documentation**: [MiniGrid Empty Space](https://minigrid.farama.org/environments/minigrid/EmptyEnv/)
minigrid environment-



![minigrid](https://github.com/user-attachments/assets/6bfc354c-2b17-4dd7-8919-39b1dbe59303)

 



 **1) Observation Space -**

  env.observation_space = { 'image': Box(0,255,(7,7,3),uint8) , 'direction':Discrete(4) ,
  'mission': "Get to the green square" }
  
  Significance of key image :
        It represents the information that the agent can perceive at any grid cell.
        The (7,7,3) matrix: at any grid cell the agent can be visualized at the center of the 
        7x7 grid ( any of those 7x7 grid cells may be behind the walls i.e. can be outside 
        the environment), these 7x7 cells can be termed as 'Vision of Agent' (at any given
        state, number of states about which the agent holds information). * The 3 in (7x7x3) 
        is for the color intensity of a particular grid cell ( among that 7x7) There are 3 
        elements in the matrix R, G, B each containing intensity in the range [0,255].

   Significance of key direction:
        The value of this can be any number in the interval [0,3] which basically tends to denote 
        the direction the agent is facing at any state.
        * 0 : Right * 1 : Down * 2 : Left * 3 : Up

   Significance of key Mission:
        It contains a string value that represents the goal of the agent.
    
 **2) Action space-**
|          |              |        
|----------|--------------|
|    0     | turn left    | 
|    1     | turn right   |
|    2     | Move forward | 

Reward Function :


  Success: A reward is calculated using the formula:
  Reward = 1 - 0.9 * (step_count / max_steps)

  Failure: A reward of 0 is given.

# **Graphs**
##1. Monte Carlo:
![minigrid_mc](https://github.com/user-attachments/assets/e944dae1-7537-426d-a573-447919f90fef)
##2. Sarsa:
![minigrid_sarsa](https://github.com/user-attachments/assets/d2d0fe28-d49d-4672-8d41-c74ef00bfec7)
##3. Sarsa(λ):
![minigrid_sarsa_lambda](https://github.com/user-attachments/assets/c84800a8-87e4-47b5-b5a9-dc3451231ac5)
##4. Q-learning:
![minigrid_q_learning](https://github.com/user-attachments/assets/a7a8c447-2b65-437f-a3d3-98c1d874552d)

## Results

### **Frozen Lake (Dynamic Programming)**:
- Policy Iteration and Value Iteration algorithms both converge relatively quickly, as the environment is simple and the state space is small (4x4 grid with 16 states).
- These algorithms explore the environment efficiently due to the known model of the environment (model-based RL).

### **MiniGrid Empty Space (Model-Free Control Algorithms)**:
- From the provided graphs, **Sarsa(λ)** converges faster than **Q-learning** due to its ability to balance exploration and exploitation more effectively.
- **Q-learning**, while effective, explores the environment more extensively and takes more steps to converge.
- **Monte Carlo** and **Sarsa** methods both perform well, but Sarsa(λ) shows better convergence under similar hyperparameter settings.



