import gym
from stable_baselines3 import PPO, DDPG, SAC, TD3, A2C
import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = ""

args = sys.argv[1:]
if (len(args) != 2):
    print("Incorrect number of arguments! Please pass Name of the algorithm, and the name of the file")
    exit()
algorithm_name = args[0]
if (algorithm_name == 'PPO'):
    algorithm = PPO
elif (algorithm_name == 'SAC'):
    algorithm = SAC
elif (algorithm_name == 'DDPG'):
    algorithm = DDPG
elif (algorithm_name == 'TD3'):
    algorithm = TD3
elif (algorithm_name == 'A2C'):
    algorithm = A2C
else:
    print("Unsupported algorithm. Available algorithms: PPO, SAC, DDPG, TD3, A2C")
    exit()

model_path = os.path.join('training', args[1])

env = gym.make('CarRacing-v1')

model = algorithm.load(model_path, env=env)

obs = env.reset()

done = False
score = 0

while True:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
    score += rewards
    if done:
        env.close()
        print(f'Score: {score}')
        break
