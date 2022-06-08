import gym
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import PPO
import os

env = gym.make('CarRacing-v1')
env = DummyVecEnv([lambda: env])

log_path = os.path.join('training', 'logs')
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=100)

ppo_path = os.path.join('training', 'ppo')
model.save(ppo_path)
