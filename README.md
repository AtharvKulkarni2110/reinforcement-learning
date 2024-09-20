# reinforcement-learning
This file consists of tasks I have done and what I learned while studying RL. This file includes an Explanation of the environments used in each task, the Graphical results after implementing various algorithms, and the Challenges I faced during implementation.


**Task 1 -Frozen Lake environment using dynamic programming:-**

  1)policy iteration using dynamic programming
  
  2)value iteration using dynamic programming
  
documentation of environment-' https://gymnasium.farama.org/environments/toy_text/frozen_lake/ '

Information about the environment:-

 **  1)Observation Space-**
     
     Consider a 4x4 map, then env.observation_space=discrete(16)
     here each state represents a whole number till 15.
     Further custom maps can be defined and each state can be labeled as either S (start) or 
     F(Frozen), H(Hole) or G(Goal).
     By default mapping, S is at 0 and G is at 15.
    
   
 **2)Action space -**
   
     there are 4 actions possible:
        0: Move left
        1: Move down
        2: Move right
        3: Move up
  **3)Rewards-**

        1 , reaching goal
        0 , otherwise


**Task 2 - Implementation of Model Free Control Algorithms in Minigrid Empty Space Environment.**

Algorithms implemented:

1. Monte-Carlo
2. Sarsa
3. Sarsa(λ)
4. Q-learning


documentation of environment-'https://minigrid.farama.org/environments/minigrid/EmptyEnv/'


Information about the environment:-

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
        Value of this can be any number in the interval [0,3] which basically tend to denote 
        the direction the agent is facing at any state.
        * 0 : Right * 1 : Down * 2 : Left * 3 : Up

          Significance of key Mission:
        It contains a string value which represents the goal of the agent.
    
 **2) Action space-**

         Actions we can take are -
           0: Turn Left
           1: Turn Right
           2: Move Forward


# **Graphs**
1. Monte Carlo:
![minigrid_mc](https://github.com/user-attachments/assets/e944dae1-7537-426d-a573-447919f90fef)
2. Sarsa:
![minigrid_sarsa](https://github.com/user-attachments/assets/d2d0fe28-d49d-4672-8d41-c74ef00bfec7)
3. Sarsa(λ):
![minigrid_sarsa_lambda](https://github.com/user-attachments/assets/c84800a8-87e4-47b5-b5a9-dc3451231ac5)
4. Q-learning:
![minigrid_q_learning](https://github.com/user-attachments/assets/a7a8c447-2b65-437f-a3d3-98c1d874552d)
 


