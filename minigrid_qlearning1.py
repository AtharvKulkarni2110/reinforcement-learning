import gym
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
Q={}                                                       # make empty dict to store q values
env = gym.make('MiniGrid-Empty-6x6-v0')
#initialize hyperparameters
num_episodes =400
alpha = 0.5
epsilon = 1.0
gamma=0.9
#to plot graphs of steps and return ,take empty list
count=[]
rt=[]
def epsilon_greedy_policy(state, Q, epsilon):
 
    if np.random.rand() < epsilon:
        return np.random.randint(0,3)  # Random action
    else:
        return np.argmax(Q[state])      #to get greedy action 
    

def plot_graphs(num_episodes,count,rt):
 plt.plot(range(num_episodes), count)
 plt.xlabel('Episode')
 plt.ylabel('Steps')
 plt.title('Steps per Episode')
 plt.show()
 plt.plot(range(num_episodes),rt)
 plt.xlabel('Episode')
 plt.ylabel('return')
 plt.title('return per Episode')
 plt.show()

for epi in range(num_episodes):                                    
    policy=[]                                                       #not used but  to know final policy
    env.reset()
    episode = []
    done = False
    steps = 0
    total_return=0
    while not done:                                    #agent takes actions till terminal state is achieved or episode is truncated midway.

        state = (tuple(env.agent_pos), env.agent_dir)    # present state 

        if state not in Q:                               # as our Q is empty initially we see if state is in dictionary otherwise initialize it .
            Q[state]=np.zeros(3)                          # our Q is now Q={tuple(tuple(agent position),direction of agent in that state):array[0,1,2],....} where 0,1,2 are actions taken in that state.
        
        action = epsilon_greedy_policy(state, Q, epsilon)   # taking action for target policy by epsilon greedy way.

        policy.append(action)

        next_obs_space, reward, done, truncated, info = env.step(action)
         # env.step(action) gives 5 attributes 1. information about next state ,2.reward obtained after taking action,3.end state is achieved or not,4.whether episode is truncated ,5.{}   
        
        next_state=(tuple(env.agent_pos),env.agent_dir)

        if next_state not in Q:                             # as our Q is empty initially we see if next state is in dictionary otherwise initialize it 
            Q[next_state]=np.zeros(3)

        Q[state][action]+=alpha*(reward+gamma*np.max(Q[next_state])-Q[state][action])     #as q learning is on-line update algo we update Q value after each action with the help of previous q value of state and behaviour policy on next state which acts always greedily 


        total_return+=gamma*reward                                            

        episode.append((state, reward, action, done,next_obs_space))

        steps += 1                                 
        if steps == 70:                                 # to truncate the episode 
            count.append(70) 
            break

        if done:                                            
            print(f"Episode finished at step {steps}")
            count.append(steps)

        state=next_state                              # update the new state as present state to take next action

    rt.append(total_return)

    epsilon = max(0.01, epsilon * 0.94)              #epsilon decay


plot_graphs(num_episodes,count,rt)    
