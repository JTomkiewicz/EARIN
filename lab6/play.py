import gym
from stable_baselines3 import PPO
import os

env = gym.make('CarRacing-v1')

ppo_path = os.path.join('Training', 'PPO_Cnn_100k')
model = PPO.load(ppo_path, env=env)

obs = env.reset()

dones = False
score = 0

while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
    score += rewards
    if dones:
        env.close()
        print(f'Score: {score}')
        break
