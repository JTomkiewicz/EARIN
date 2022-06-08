import gym

env = gym.make('CarRacing-v1')

env.reset()
env.close()

episodes = 5

for episode in range(1, episodes+1):
    obs = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        score += reward

    print(f'Episode {episode} score: {score}')

env.close()
