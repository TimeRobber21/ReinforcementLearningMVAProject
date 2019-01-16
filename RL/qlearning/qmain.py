#import keyboard as kb
import sys

sys.path.append('../../utils')

import time
from qagent import *
import matplotlib.pyplot as plt
import reward as rd
from tqdm import tqdm

data_path = 'reward_params_15_15.txt'

env = gym.make('MountainCar-v0')
write_path = 'data_long.txt'
T = 1000
N = 20

qa = QAgent(env, T)

reward = rd.Reward(15, 15, env)
reward.import_from_file(data_path)

qa_r = QAgent(env, T, reward_fun=reward)

#qa.episode(1, render=True)

lengths = np.zeros(2000)
lengths_r = np.zeros(2000)

for i in tqdm(range(N)):
    qa.reset()
    qa_r.reset()
    lengths += np.asarray(qa.q_learn(2000))
    lengths_r += np.asarray(qa_r.q_learn(2000))

lengths = 1/N * lengths
lengths_r = 1/N * lengths_r

trajs = qa.generate_trajectories(50)

plt.plot([length for length in lengths])
plt.plot([length for length in lengths_r])
plt.show()
'''
proceed = input('Proceed to trajectory generation ?')

if proceed == 'y':
    qa.generate_trajectory_file(200, write_path)
else:
    qa.q_learn(20000)
'''
env.close()



