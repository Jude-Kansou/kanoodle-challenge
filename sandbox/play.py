# sandbox/play.py
from stable_baselines3 import PPO
from puzzle.env import KanoodleEnv

env   = KanoodleEnv(render_mode="human")
model = PPO.load("models/best_model")   # or ppo_kanoodle_final

obs, info = env.reset()
done = False
while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, info = env.step(action)
env.render()
