import numpy as np
import os
import glob

def load_winners_dataset(data_folder="data"):
    """
    Loads .npz logs and builds (s, a, r, s', done) transitions
    using ONLY the winner’s perspective.
    Sensors are reduced to 3 values:
      [min(dat1, dat2, dat3), dat4, dat5]

    Returns:
      states, actions, rewards, next_states, dones
    """
    all_states, all_actions, all_rewards, all_next_states, all_dones = [], [], [], [], []

    files = glob.glob(os.path.join(data_folder, "*.npz"))
    print(f"Found {len(files)} game files.")

    for fpath in files:
        fname = os.path.basename(fpath)
        winner = int(fname.split("_")[0][0])  # winner encoded in filename

        data = np.load(fpath, allow_pickle=True)

        prefix = f"P{winner}_dat"
        sensors = [data[f"{prefix}{i}"] for i in range(1, 6)]  # dat1..5
        actions = data[f"Klavish_{winner}"]

        # Shape sensors into (T, 3)
        dat1, dat2, dat3, dat4, dat5 = sensors
        front_min = np.minimum.reduce([dat1, dat2, dat3])
        states = np.stack([front_min, dat4, dat5], axis=1)

        T = len(actions)

        # Rewards: 0 everywhere, +1 at final step
        rewards = np.zeros(T, dtype=np.float32)
        rewards[-1] = 1.0

        for t in range(T - 1):
            s = states[t]
            a = actions[t]
            r = rewards[t]
            s_next = states[t + 1]
            done = 0.0

            # ⚡ punish standing still
            if np.array_equal(a, [0, 0]):
                r = -0.2

            # ⚡ punish backing away if enemy close
            if (a[0] == -1 or a[1] == -1) and s[0] < 30:
                r = -0.5

            # ⚡ reward attacking forward if enemy close
            if (a[0] == 1 or a[1] == 1) and s[0] < 30:
                r = +0.3

            all_states.append(s)
            all_actions.append(a)
            all_rewards.append(r)
            all_next_states.append(s_next)
            all_dones.append(done)

        # Final transition → terminal
        s = states[-1]
        a = actions[-1]
        r = rewards[-1]
        s_next = states[-1]
        done = 1.0

        all_states.append(s)
        all_actions.append(a)
        all_rewards.append(r)
        all_next_states.append(s_next)
        all_dones.append(done)

    # Convert to arrays
    states = np.array(all_states, dtype=np.float32)
    actions = np.array(all_actions, dtype=np.int32)
    rewards = np.array(all_rewards, dtype=np.float32)
    next_states = np.array(all_next_states, dtype=np.float32)
    dones = np.array(all_dones, dtype=np.float32)

    print(f"Dataset built (winners only): {states.shape[0]} transitions, state_dim = {states.shape[1]}")
    return states, actions, rewards, next_states, dones

# Load dataset from winners only
states, actions, rewards, next_states, dones = load_winners_dataset("data")

print(states.shape)       # (N, 3)  -> 3 sensors
print(actions.shape)      # (N,)
print(rewards.shape)      # (N,)
print(next_states.shape)  # (N, 3)
print(dones.shape)        # (N,)
