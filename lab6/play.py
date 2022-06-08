import gym
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO
import os

env = gym.make('CarRacing-v1')
env = DummyVecEnv([lambda: env])

ppo_path = os.path.join('training', 'PPO_Cnn_100k')
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
