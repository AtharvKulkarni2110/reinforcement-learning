import numpy as np
import gym
import pygame
import time

def value_iteration(P, nS, nA,prev_valuefxn,gamma=0.9, tol=1e-3):
    """
        Learn value function and policy by using value iteration method for a given
        gamma and environment.

        Parameters:
        ----------
        P, nS, nA, gamma:
            defined at beginning of file
        tol: float
            Terminate value iteration when
                max |value_function(s) - prev_value_function(s)| < tol
        Returns:
        ----------
        value_function: np.ndarray[nS]
        policy: np.ndarray[nS]
        """
    value_function = np.zeros(nS)
    policy = np.zeros(nS, dtype=int)
    count=0
    delta = float('inf')
    ############################
    # YOUR IMPLEMENTATION HERE #
    while delta > tol:
        delta = 0
        for s in range(nS):
            state_values=np.zeros(nA)
            for a in range(nA):
             for probability, nextstate, reward, _ in P[s][a]:
                 state_values[a]+= probability * (reward + gamma * prev_valuefxn[nextstate])
            value_function[s]=np.max(state_values)
            delta = max(delta, np.abs(value_function[s] - prev_valuefxn[s]))
            policy[s]=np.argmax(state_values)
        for j in range (nS):
            prev_valuefxn[j]=value_function[j] 
        count+=1
        if delta<tol:
            print("total iterations took to terminate ",count)
            break



    ############################
    return value_function, policy
def render_single(env, policy, max_steps=100):
    """
      This function does not need to be modified
      Renders policy once on environment. Watch your agent play!

      Parameters
      ----------
      env: gym.core.Environment
        Environment to play on. Must have nS, nA, and P as
        attributes.
      Policy: np.array of shape [env.nS]
        The action to take at a given state
    """
    episode_reward = 0
    ob = env.reset()
    ob = ob[0]            # Try this or Comment this based on [doing in Colab or VsCode]
    for t in range(max_steps):
        env.render()
        time.sleep(0.25)
        a = policy[ob]
        ob, rew, done, _ ,_= env.step(a)       # remove a blank after done if on Colab 
        episode_reward += rew
        if done:
            break
    env.render()
    if not done:
        print("The agent didn't reach a terminal state in {} steps.".format(max_steps))
    else:
        print("Episode reward: %f" % episode_reward)

if __name__ == "__main__":
    #name = "FrozenLake8x8-v1"
    name = "FrozenLake-v1"
    is_slippery = False
    if(name == "FrozenLake8x8-v1"):
        P={0: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 8, 0.0, False)], 2: [(1.0, 1, 0.0, False)], 3: [(1.0, 0, 0.0, False)]}, 1: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 9, 0.0, False)], 2: [(1.0, 2, 0.0, False)], 3: [(1.0, 1, 0.0, False)]}, 2: {0: [(1.0, 1, 0.0, False)], 1: [(1.0, 10, 0.0, False)], 2: [(1.0, 3, 0.0, False)], 3: [(1.0, 2, 0.0, False)]}, 3: {0: [(1.0, 2, 0.0, False)], 1: [(1.0, 11, 0.0, False)], 2: [(1.0, 4, 0.0, False)], 3: [(1.0, 3, 0.0, False)]}, 4: {0: [(1.0, 3, 0.0, False)], 1: [(1.0, 12, 0.0, False)], 2: [(1.0, 5, 0.0, False)], 3: [(1.0, 4, 0.0, False)]}, 5: {0: [(1.0, 4, 0.0, False)], 1: [(1.0, 13, 0.0, False)], 2: [(1.0, 6, 0.0, False)], 3: [(1.0, 5, 0.0, False)]}, 6: {0: [(1.0, 5, 0.0, False)], 1: [(1.0, 14, 0.0, False)], 2: [(1.0, 7, 0.0, False)], 3: [(1.0, 6, 0.0, False)]}, 7: {0: [(1.0, 6, 0.0, False)], 1: [(1.0, 15, 0.0, False)], 2: [(1.0, 7, 0.0, False)], 3: [(1.0, 7, 0.0, False)]}, 8: {0: [(1.0, 8, 0.0, False)], 1: [(1.0, 16, 0.0, False)], 2: [(1.0, 9, 0.0, False)], 3: [(1.0, 0, 0.0, False)]}, 9: {0: [(1.0, 8, 0.0, False)], 1: [(1.0, 17, 0.0, False)], 2: [(1.0, 10, 0.0, False)], 3: [(1.0, 1, 0.0, False)]}, 10: {0: [(1.0, 9, 0.0, False)], 1: [(1.0, 18, 0.0, False)], 2: [(1.0, 11, 0.0, False)], 3: [(1.0, 2, 0.0, False)]}, 11: {0: [(1.0, 10, 0.0, False)], 1: [(1.0, 19, 0.0, True)], 2: [(1.0, 12, 0.0, False)], 3: [(1.0, 3, 0.0, False)]}, 12: {0: [(1.0, 11, 0.0, False)], 1: [(1.0, 20, 0.0, False)], 2: [(1.0, 13, 0.0, False)], 3: [(1.0, 4, 0.0, False)]}, 13: {0: [(1.0, 12, 0.0, False)], 1: [(1.0, 21, 0.0, False)], 2: [(1.0, 14, 0.0, False)], 3: [(1.0, 5, 0.0, False)]}, 14: {0: [(1.0, 13, 0.0, False)], 1: [(1.0, 22, 0.0, False)], 2: [(1.0, 15, 0.0, False)], 3: [(1.0, 6, 0.0, False)]}, 15: {0: [(1.0, 14, 0.0, False)], 1: [(1.0, 23, 0.0, False)], 2: [(1.0, 15, 0.0, False)], 3: [(1.0, 7, 0.0, False)]}, 16: {0: [(1.0, 16, 0.0, False)], 1: [(1.0, 24, 0.0, False)], 2: [(1.0, 17, 0.0, False)], 3: [(1.0, 8, 0.0, False)]}, 17: {0: [(1.0, 16, 0.0, False)], 1: [(1.0, 25, 0.0, False)], 2: [(1.0, 18, 0.0, False)], 3: [(1.0, 9, 0.0, False)]}, 18: {0: [(1.0, 17, 0.0, False)], 1: [(1.0, 26, 0.0, False)], 2: [(1.0, 19, 0.0, True)], 3: [(1.0, 10, 0.0, False)]}, 19: {0: [(1.0, 19, 0, True)], 1: [(1.0, 19, 0, True)], 2: [(1.0, 19, 0, True)], 3: [(1.0, 19, 0, True)]}, 20: {0: [(1.0, 19, 0.0, True)], 1: [(1.0, 28, 0.0, False)], 2: [(1.0, 21, 0.0, False)], 3: [(1.0, 12, 0.0, False)]}, 21: {0: [(1.0, 20, 0.0, False)], 1: [(1.0, 29, 0.0, True)], 2: [(1.0, 22, 0.0, False)], 3: [(1.0, 13, 0.0, False)]}, 22: {0: [(1.0, 21, 0.0, False)], 1: [(1.0, 30, 0.0, False)], 2: [(1.0, 23, 0.0, False)], 3: [(1.0, 14, 0.0, False)]}, 23: {0: [(1.0, 22, 0.0, False)], 1: [(1.0, 31, 0.0, False)], 2: [(1.0, 23, 0.0, False)], 3: [(1.0, 15, 0.0, False)]}, 24: {0: [(1.0, 24, 0.0, False)], 1: [(1.0, 32, 0.0, False)], 2: [(1.0, 25, 0.0, False)], 3: [(1.0, 16, 0.0, False)]}, 25: {0: [(1.0, 24, 0.0, False)], 1: [(1.0, 33, 0.0, False)], 2: [(1.0, 26, 0.0, False)], 3: [(1.0, 17, 0.0, False)]}, 26: {0: [(1.0, 25, 0.0, False)], 1: [(1.0, 34, 0.0, False)], 2: [(1.0, 27, 0.0, False)], 3: [(1.0, 18, 0.0, False)]}, 27: {0: [(1.0, 26, 0.0, False)], 1: [(1.0, 35, 0.0, True)], 2: [(1.0, 28, 0.0, False)], 3: [(1.0, 19, 0.0, True)]}, 28: {0: [(1.0, 27, 0.0, False)], 1: [(1.0, 36, 0.0, False)], 2: [(1.0, 29, 0.0, True)], 3: [(1.0, 20, 0.0, False)]}, 29: {0: [(1.0, 29, 0, True)], 1: [(1.0, 29, 0, True)], 2: [(1.0, 29, 0, True)], 3: [(1.0, 29, 0, True)]}, 30: {0: [(1.0, 29, 0.0, True)], 1: [(1.0, 38, 0.0, False)], 2: [(1.0, 31, 0.0, False)], 3: [(1.0, 22, 0.0, False)]}, 31: {0: [(1.0, 30, 0.0, False)], 1: [(1.0, 39, 0.0, False)], 2: [(1.0, 31, 0.0, False)], 3: [(1.0, 23, 0.0, False)]}, 32: {0: [(1.0, 32, 0.0, False)], 1: [(1.0, 40, 0.0, False)], 2: [(1.0, 33, 0.0, False)], 3: [(1.0, 24, 0.0, False)]}, 33: {0: [(1.0, 32, 0.0, False)], 1: [(1.0, 41, 0.0, True)], 2: [(1.0, 34, 0.0, False)], 3: [(1.0, 25, 0.0, False)]}, 34: {0: [(1.0, 33, 0.0, False)], 1: [(1.0, 42, 0.0, True)], 2: [(1.0, 35, 0.0, True)], 3: [(1.0, 26, 0.0, False)]}, 35: {0: [(1.0, 35, 0, True)], 1: [(1.0, 35, 0, True)], 2: [(1.0, 35, 0, True)], 3: [(1.0, 35, 0, True)]}, 36: {0: [(1.0, 35, 0.0, True)], 1: [(1.0, 44, 0.0, False)], 2: [(1.0, 37, 0.0, False)], 3: [(1.0, 28, 0.0, False)]}, 37: {0: [(1.0, 36, 0.0, False)], 1: [(1.0, 45, 0.0, False)], 2: [(1.0, 38, 0.0, False)], 3: [(1.0, 29, 0.0, True)]}, 38: {0: [(1.0, 37, 0.0, False)], 1: [(1.0, 46, 0.0, True)], 2: [(1.0, 39, 0.0, False)], 3: [(1.0, 30, 0.0, False)]}, 39: {0: [(1.0, 38, 0.0, False)], 1: [(1.0, 47, 0.0, False)], 2: [(1.0, 39, 0.0, False)], 3: [(1.0, 31, 0.0, False)]}, 40: {0: [(1.0, 40, 0.0, False)], 1: [(1.0, 48, 0.0, False)], 2: [(1.0, 41, 0.0, True)], 3: [(1.0, 32, 0.0, False)]}, 41: {0: [(1.0, 41, 0, True)], 1: [(1.0, 41, 0, True)], 2: [(1.0, 41, 0, True)], 3: [(1.0, 41, 0, True)]}, 42: {0: [(1.0, 42, 0, True)], 1: [(1.0, 42, 0, True)], 2: [(1.0, 42, 0, True)], 3: [(1.0, 42, 0, True)]}, 43: {0: [(1.0, 42, 0.0, True)], 1: [(1.0, 51, 0.0, False)], 2: [(1.0, 44, 0.0, False)], 3: [(1.0, 35, 0.0, True)]}, 44: {0: [(1.0, 43, 0.0, False)], 1: [(1.0, 52, 0.0, True)], 2: [(1.0, 45, 0.0, False)], 3: [(1.0, 36, 0.0, False)]}, 45: {0: [(1.0, 44, 0.0, False)], 1: [(1.0, 53, 0.0, False)], 2: [(1.0, 46, 0.0, True)], 3: [(1.0, 37, 0.0, False)]}, 46: {0: [(1.0, 46, 0, True)], 1: [(1.0, 46, 0, True)], 2: [(1.0, 46, 0, True)], 3: [(1.0, 46, 0, True)]}, 47: {0: [(1.0, 46, 0.0, True)], 1: [(1.0, 55, 0.0, False)], 2: [(1.0, 47, 0.0, False)], 3: [(1.0, 39, 0.0, False)]}, 48: {0: [(1.0, 48, 0.0, False)], 1: [(1.0, 56, 0.0, False)], 2: [(1.0, 49, 0.0, True)], 3: [(1.0, 40, 0.0, False)]}, 49: {0: [(1.0, 49, 0, True)], 1: [(1.0, 49, 0, True)], 2: [(1.0, 49, 0, True)], 3: [(1.0, 49, 0, True)]}, 50: {0: [(1.0, 49, 0.0, True)], 1: [(1.0, 58, 0.0, False)], 2: [(1.0, 51, 0.0, False)], 3: [(1.0, 42, 0.0, True)]}, 51: {0: [(1.0, 50, 0.0, False)], 1: [(1.0, 59, 0.0, True)], 2: [(1.0, 52, 0.0, True)], 3: [(1.0, 43, 0.0, False)]}, 52: {0: [(1.0, 52, 0, True)], 1: [(1.0, 52, 0, True)], 2: [(1.0, 52, 0, True)], 3: [(1.0, 52, 0, True)]}, 53: {0: [(1.0, 52, 0.0, True)], 1: [(1.0, 61, 0.0, False)], 2: [(1.0, 54, 0.0, True)], 3: [(1.0, 45, 0.0, False)]}, 54: {0: [(1.0, 54, 0, True)], 1: [(1.0, 54, 0, True)], 2: [(1.0, 54, 0, True)], 3: [(1.0, 54, 0, True)]}, 55: {0: [(1.0, 54, 0.0, True)], 1: [(1.0, 63, 1.0, True)], 2: [(1.0, 55, 0.0, False)], 3: [(1.0, 47, 0.0, False)]}, 56: {0: [(1.0, 56, 0.0, False)], 1: [(1.0, 56, 0.0, False)], 2: [(1.0, 57, 0.0, False)], 3: [(1.0, 48, 0.0, False)]}, 57: {0: [(1.0, 56, 0.0, False)], 1: [(1.0, 57, 0.0, False)], 2: [(1.0, 58, 0.0, False)], 3: [(1.0, 49, 0.0, True)]}, 58: {0: [(1.0, 57, 0.0, False)], 1: [(1.0, 58, 0.0, False)], 2: [(1.0, 59, 0.0, True)], 3: [(1.0, 50, 0.0, False)]}, 59: {0: [(1.0, 59, 0, True)], 1: [(1.0, 59, 0, True)], 2: [(1.0, 59, 0, True)], 3: [(1.0, 59, 0, True)]}, 60: {0: [(1.0, 59, 0.0, True)], 1: [(1.0, 60, 0.0, False)], 2: [(1.0, 61, 0.0, False)], 3: [(1.0, 52, 0.0, True)]}, 61: {0: [(1.0, 60, 0.0, False)], 1: [(1.0, 61, 0.0, False)], 2: [(1.0, 62, 0.0, False)], 3: [(1.0, 53, 0.0, False)]}, 62: {0: [(1.0, 61, 0.0, False)], 1: [(1.0, 62, 0.0, False)], 2: [(1.0, 63, 1.0, True)], 3: [(1.0, 54, 0.0, True)]}, 63: {0: [(1.0, 63, 0, True)], 1: [(1.0, 63, 0, True)], 2: [(1.0, 63, 0, True)], 3: [(1.0, 63, 0, True)]}}
        nS=64
        nA=4

    else:
        P= {0: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 4, 0.0, False)], 2: [(1.0, 1, 0.0, False)], 3: [(1.0, 0, 0.0, False)]}, 1: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 5, 0.0, True)], 2: [(1.0, 2, 0.0, False)], 3: [(1.0, 1, 0.0, False)]}, 2: {0: [(1.0, 1, 0.0, False)], 1: [(1.0, 6, 0.0, False)], 2: [(1.0, 3, 0.0, False)], 3: [(1.0, 2, 0.0, False)]}, 3: {0: [(1.0, 2, 0.0, False)], 1: [(1.0, 7, 0.0, True)], 2: [(1.0, 3, 0.0, False)], 3: [(1.0, 3, 0.0, False)]}, 4: {0: [(1.0, 4, 0.0, False)], 1: [(1.0, 8, 0.0, False)], 2: [(1.0, 5, 0.0, True)], 3: [(1.0, 0, 0.0, False)]}, 5: {0: [(1.0, 5, 0, True)], 1: [(1.0, 5, 0, True)], 2: [(1.0, 5, 0, True)], 3: [(1.0, 5, 0, True)]}, 6: {0: [(1.0, 5, 0.0, True)], 1: [(1.0, 10, 0.0, False)], 2: [(1.0, 7, 0.0, True)], 3: [(1.0, 2, 0.0, False)]}, 7: {0: [(1.0, 7, 0, True)], 1: [(1.0, 7, 0, True)], 2: [(1.0, 7, 0, True)], 3: [(1.0, 7, 0, True)]}, 8: {0: [(1.0, 8, 0.0, False)], 1: [(1.0, 12, 0.0, True)], 2: [(1.0, 9, 0.0, False)], 3: [(1.0, 4, 0.0, False)]}, 9: {0: [(1.0, 8, 0.0, False)], 1: [(1.0, 13, 0.0, False)], 2: [(1.0, 10, 0.0, False)], 3: [(1.0, 5, 0.0, True)]}, 10: {0: [(1.0, 9, 0.0, False)], 1: [(1.0, 14, 0.0, False)], 2: [(1.0, 11, 0.0, True)], 3: [(1.0, 6, 0.0, False)]}, 11: {0: [(1.0, 11, 0, True)], 1: [(1.0, 11, 0, True)], 2: [(1.0, 11, 0, True)], 3: [(1.0, 11, 0, True)]}, 12: {0: [(1.0, 12, 0, True)], 1: [(1.0, 12, 0, True)], 2: [(1.0, 12, 0, True)], 3: [(1.0, 12, 0, True)]}, 13: {0: [(1.0, 12, 0.0, True)], 1: [(1.0, 13, 0.0, False)], 2: [(1.0, 14, 0.0, False)], 3: [(1.0, 9, 0.0, False)]}, 14: {0: [(1.0, 13, 0.0, False)], 1: [(1.0, 14, 0.0, False)], 2: [(1.0, 15, 1.0, True)], 3: [(1.0, 10, 0.0, False)]}, 15: {0: [(1.0, 15, 0, True)], 1: [(1.0, 15, 0, True)], 2: [(1.0, 15, 0, True)], 3: [(1.0, 15, 0, True)]}}
        nS=16
        nA=4
        if is_slippery==True:
            P = {0: {0: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False)], 1: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 1, 0.0, False)], 2: [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False)], 3: [(0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 0, 0.0, False)]}, 1: {0: [(0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 5, 0.0, True)], 1: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 2, 0.0, False)], 2: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False)], 3: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False)]}, 2: {0: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 6, 0.0, False)], 1: [(0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 3, 0.0, False)], 2: [(0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False)], 3: [(0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False)]}, 3: {0: [(0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 7, 0.0, True)], 1: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 3, 0.0, False)], 2: [(0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 3, 0.0, False)], 3: [(0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False)]}, 4: {0: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False)], 1: [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 5, 0.0, True)], 2: [(0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 0, 0.0, False)], 3: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False)]}, 5: {0: [(1.0, 5, 0, True)], 1: [(1.0, 5, 0, True)], 2: [(1.0, 5, 0, True)], 3: [(1.0, 5, 0, True)]}, 6: {0: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 10, 0.0, False)], 1: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 7, 0.0, True)], 2: [(0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 2, 0.0, False)], 3: [(0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 5, 0.0, True)]}, 7: {0: [(1.0, 7, 0, True)], 1: [(1.0, 7, 0, True)], 2: [(1.0, 7, 0, True)], 3: [(1.0, 7, 0, True)]}, 8: {0: [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 12, 0.0, True)], 1: [(0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 9, 0.0, False)], 2: [(0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 4, 0.0, False)], 3: [(0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False)]}, 9: {0: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 13, 0.0, False)], 1: [(0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 10, 0.0, False)], 2: [(0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 5, 0.0, True)], 3: [(0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 8, 0.0, False)]}, 10: {0: [(0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 14, 0.0, False)], 1: [(0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 11, 0.0, True)], 2: [(0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 11, 0.0, True), (0.3333333333333333, 6, 0.0, False)], 3: [(0.3333333333333333, 11, 0.0, True), (0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 9, 0.0, False)]}, 11: {0: [(1.0, 11, 0, True)], 1: [(1.0, 11, 0, True)], 2: [(1.0, 11, 0, True)], 3: [(1.0, 11, 0, True)]}, 12: {0: [(1.0, 12, 0, True)], 1: [(1.0, 12, 0, True)], 2: [(1.0, 12, 0, True)], 3: [(1.0, 12, 0, True)]}, 13: {0: [(0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 13, 0.0, False)], 1: [(0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False)], 2: [(0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 9, 0.0, False)], 3: [(0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 12, 0.0, True)]}, 14: {0: [(0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False)], 1: [(0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 15, 1.0, True)], 2: [(0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 15, 1.0, True), (0.3333333333333333, 10, 0.0, False)], 3: [(0.3333333333333333, 15, 1.0, True), (0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 13, 0.0, False)]}, 15: {0: [(1.0, 15, 0, True)], 1: [(1.0, 15, 0, True)], 2: [(1.0, 15, 0, True)], 3: [(1.0, 15, 0, True)]}}

    # Make gym environment
    env = gym.make(name,is_slippery=False,render_mode='human')
    # env.reset()
    # env.render()
    prev_valuefxn = np.zeros(nS)

    print("\n" + "-" * 25 + "\nBeginning Value Iteration\n" + "-" * 25)

    V_pi, p_pi = value_iteration(P, nS, nA,prev_valuefxn, gamma=0.9, tol=1e-3)
    print(V_pi)
    print(p_pi)
    render_single(env, p_pi, 100)