# sandbox/main.py
from puzzle.env import KanoodleEnv

def demo():
    env = KanoodleEnv()
    obs, info = env.reset()
    done = False
    moves = 0
    total_reward = 0.0

    while not done:
        mask = info["action_mask"]
        if not mask.any():          # no legal moves left ⇒ give up
            print("No further moves possible — giving up.")
            break

        action = env.action_space.sample(mask=mask)
        obs, reward, done, _, info = env.step(action)
        moves += 1
        total_reward += reward

    print(f"Episode finished after {moves} moves.  Total reward: {total_reward:.2f}")
    env.render()                    # prints the final board

if __name__ == "__main__":
    demo()
