import gym
import gym_kuiper_escape
import random as rnd
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

import math
env = gym.make('kuiper-escape-base-v0',mode='None',rock_rate=0.2,player_speed=0.5,rock_size_min=0.08,rock_size_max=0.1)
Q={}
num_episodes=10000                                             #define number of episodes to train
# testcase=500
alpha=0.7
epsilon=1
gamma=0.8
count=[]
rt=[]
test=[]
test_return=[]

def epsilon_greedy_policy(state, Q, epsilon):
 
    if np.random.rand() < epsilon:
        return np.random.randint(0,5)                         # Random action
    else:
        return np.argmax(Q[state])                            #to get greedy action 
    
def sma(rt,num_episodes) :                                    # Plotting simple moving average of total return                           
  Sma=[]
  
  for i in range (num_episodes) :
   B=0
   for j in range (i-50, i):
     if j>=0 and j<num_episodes:
        B+=rt[j]
   Sma.append(B/50) 
  return Sma    

def plot_graphs(episodes, iterations, total_reward,Sma):     #plotting graphs
    plt.figure(figsize=(12, 5),dpi=200)
    
    plt.subplot(1, 2, 1)
    plt.plot(range(episodes), iterations)
    plt.xlabel('Episode')
    plt.ylabel('Steps')
    plt.title('Steps per Episode')
    
    plt.subplot(1, 2, 2)
    plt.plot(range(episodes), total_reward)
    plt.plot(range(num_episodes), Sma,color='red') 
    plt.grid()
    plt.xlabel('Episode')
    plt.ylabel('Return')
    plt.title('Return per Episode')
    
    plt.tight_layout()
    
    try:
        # Save the plots
        plt.savefig(f'training_plots_and_sma1{episodes}.png')

    except Exception as e:
        print(f"Error with plot: {e}")
    finally:
        plt.close()



max_steps = 3000                                            

for episode in range (num_episodes):
    ini_observation=env.reset()
    state=tuple(ini_observation)                             #converting observation space into tuple for hashing purpose
    slope=(1)/num_episodes                                   

    done = False
    iterations=0

    if (episode%1000==1):          
       print(f'Epi:{episode} , Reward:{total_return}')
    total_return=0
    while not done and iterations<max_steps:                  #Take actions till it collides or reaches max iterations

        if state not in Q:
           Q[state]=np.zeros(5,dtype=float)                   #for 1st visit initializing Q table for current state

        action=epsilon_greedy_policy(state,Q,epsilon)        #Take epsilon greedy action

        observation,reward,done,info=env.step(action)        


        
        if done:
           reward = -5                                         # negative reward for collision with rock

        iterations+=1


        next_state=tuple(observation)

        if next_state not in Q:
           Q[next_state]=np.zeros(5)


        Q[state][action]+=alpha*(reward+gamma*np.max(Q[next_state])-Q[state][action])    #Q value update for give state-action pair

        total_return+=reward



        state=next_state

    count.append(iterations)
    rt.append(total_return)


    # epsilon=max(0.01, epsilon * 0.95)
    # epsilon=epsilon_min+(epsilon_max-epsilon_min)/(1+np.exp(-k*(episode-t0)))
    epsilon=1-1.7*episode/num_episodes                                                   #Using linear epsilon decay to balance exploration and exploitation in such vast environment
    # alpha=alpha-episode*slope 
 
Sma=sma(rt, num_episodes)
plot_graphs(num_episodes,count,rt,Sma)


