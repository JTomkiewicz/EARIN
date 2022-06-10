import gym
from stable_baselines3 import PPO, DDPG, SAC, TD3, A2C
import os
import time
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = ""

args = sys.argv[1:]
if len(args) != 3 and len(args) != 4:
    print(len(args))
    print(args)
    print(
        "Incorrect number of arguments! Please pass Name of the algorithm, number of action steps of training, name of the output file and optionaly name of the model you wish to continue training"
    )
    exit()
algorithm_name = args[0]
if algorithm_name == "PPO":
    algorithm = PPO
elif algorithm_name == "SAC":
    algorithm = SAC
elif algorithm_name == "DDPG":
    algorithm = DDPG
elif algorithm_name == "TD3":
    algorithm = TD3
elif algorithm_name == "A2C":
    algorithm = A2C
else:
    print("Unsupported algorithm. Available algorithms: PPO, SAC, DDPG, TD3, A2C")
    exit()

env = gym.make("CarRacing-v1")

timesteps = int(args[1])
write_path = os.path.join("training", args[2])
if len(args) == 4:
    read_path = os.path.join("training", args[3])
    model = algorithm.load(read_path, env=env)
else:
    model = algorithm("CnnPolicy", env, verbose=1)


start_time = time.time()

model.learn(total_timesteps=timesteps, reset_num_timesteps=False)
end_time = time.time()
print(f"Training time: {end_time - start_time}")
model.save(write_path)
