# sandbox/learn.py
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback
from puzzle.env import KanoodleEnv

def main():
    train_env = KanoodleEnv()
    eval_env  = KanoodleEnv()

    model = PPO(
        "MultiInputPolicy",          # <-- change from "MlpPolicy"
        train_env,
        verbose=1,
        tensorboard_log="runs/ppo_kanoodle",
        learning_rate=3e-4,
        n_steps=1024,
        batch_size=512,
        gamma=0.99,
        # (optional) bigger net for the grid + available-vector:
        # policy_kwargs=dict(net_arch=[256, 256])
    )

    eval_cb = EvalCallback(
        eval_env,
        best_model_save_path="models/",
        log_path="logs/",
        eval_freq=10_000,
        n_eval_episodes=20,
        deterministic=True,
        warn=False,
    )

    model.learn(total_timesteps=100_000, callback=eval_cb)
    model.save("models/ppo_kanoodle_final")
    print("Training complete!  Model saved to models/")

if __name__ == "__main__":
    main()
