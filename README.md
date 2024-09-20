# reinforcement-learning
This file consists of tasks I have done and what I learned while studying RL. This file includes an Explanation of the environments used in each task, the Graphical results after implementing various algorithms, and the Challenges I faced during implementation.


##Task 1 -Frozen Lake environment using dynamic programming:-

  1)policy iteration using dynamic programming
  
  2)value iteration using dynamic programming
  
documentation of environment-' https://gymnasium.farama.org/environments/toy_text/frozen_lake/ '

Information about the environment:-

   1)**Observation Space-**
     
     Consider a 4x4 map, then env.observation_space=discrete(16)
     here each state represents a whole number till 15.
     Further custom maps can be defined and each state can be labeled as either S (start) or 
     F(Frozen), H(Hole) or G(Goal).
     By default mapping, S is at 0 and G is at 15.
    
   
   2)**Action space -**
   
     there are 4 actions possible:
        0: Move left
        1: Move down
        2: Move right
        3: Move up
   3)**Rewards-**

        1 , reaching goal
        0 , otherwise

    
