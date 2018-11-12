import gym
import torch
import numpy as np

from maml_rl.episode import BatchEpisodes

def make_env(env_name):
    def _make_env():
        return gym.make(env_name)
    return _make_env

class UnityBatchSampler(object):
    def __init__(self, env_name, batch_size, num_workers=1):
        self.env_name = env_name
        self.batch_size = batch_size
        
        self.envs = gym.make(env_name)
        self.num_workers = self.envs.number_agents
        # self._env = gym.make(env_name)

    def sample(self, policy, params=None, gamma=0.95, device='cpu'):
        episodes = BatchEpisodes(batch_size=self.batch_size, gamma=gamma, device=device)
        observations = self.envs.reset()
        observations = np.float32(observations)
        done_count = 0
        indexs = list(range(self.num_workers))
        next_index = self.num_workers
        while (done_count < self.batch_size):
            with torch.no_grad():
                observations_tensor = torch.from_numpy(observations).to(device=device)
                actions_tensor = policy(observations_tensor, params=params).sample()
                actions = actions_tensor.cpu().numpy()
            new_observations, rewards, dones, _ = self.envs.step(actions)
            new_observations = np.float32(new_observations)
            rewards = np.float32(rewards)
            episodes.append(observations, actions, rewards, indexs)
            observations = new_observations
            for i, done in enumerate(dones):
                if done:
                    done_count = done_count + 1
                    if next_index >= self.batch_size or indexs[i] is None:
                        indexs[i] = None
                    else:
                        indexs[i] = next_index
                        next_index = next_index + 1
        return episodes

    def reset_task(self, task):
        tasks = [task for _ in range(self.num_workers)]
        return self.envs.reset_tasks(tasks)

    def sample_tasks(self, num_tasks):
        tasks = self.envs.sample_tasks(num_tasks)
        return tasks
