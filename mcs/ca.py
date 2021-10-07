import numpy as np
import matplotlib.pyplot as plt

from .mcs import MCS


class CA(MCS):
    """Cellular automata simulation.

    Override this class to customize conﬁguration and
    state-transition function.

    Attributes:
        max_step: The max step.
        size_x: Number of cells in x dimension.
        size_y: Number of cells in y dimension.
        seed: NumPy random seed.
        s: An array of shape (max_step, size_x) or (max_step, size_y, size_x)
        representing the states.
        step: The current step.
    """
    def __init__(self, max_step, size_x, size_y=1, seed=42):
        super().__init__(max_step)
        self.size_x = size_x
        self.size_y = size_y
        self.seed = seed
        if size_y == 1:
            self.s = np.zeros((max_step, size_x))
        else:
            self.s = np.zeros((max_step, size_y, size_x))

    def initialize(self):
        """Sets up the initial conﬁguration."""
        np.random.seed(self.seed)
        self.s[0] = np.random.randint(2, size=self.s[0].shape)

    def update(self, F):
        """Updates the states in the next step.

        Args:
            F: A state transition function which returns an array.
        """
        config = self.s[self.step]
        self.step += 1
        self.s[self.step] = F(config)

    @staticmethod
    def rule184(config):
        assert config.ndim == 1
        size = len(config)
        config_next = np.zeros(size)
        neighborhoods = set([(1, 1, 1), (1, 0, 1), (1, 0, 0), (0, 1, 1)])
        for x in range(size):
            pattern = (config[(x-1) % size], config[x], config[(x+1) % size])
            if pattern in neighborhoods:
                config_next[x] = 1
        return config_next

    @staticmethod
    def game_of_life(config):
        assert config.ndim == 2
        size_y, size_x = config.shape
        config_next = np.zeros(config.shape)
        for y in range(size_y):
            for x in range(size_x):
                state = config[y, x]
                num_alive = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        num_alive += config[(y+dy) % size_y, (x+dx) % size_x]
                if state == 0 and num_alive == 3:
                    state = 1
                elif state == 1 and (num_alive < 3 or num_alive > 4):
                    state = 0
                config_next[y, x] = state
        return config_next

    def visualize(self, step=-1):
        """Visualizes the states of the system using an image of
        shape (step, size_x) or (size_y, size_x).

        Args:
            step: The step to plot.
        Returns:
            A matplotlib.figure.Figure object.
        """
        fig, ax = plt.subplots()
        if self.s.ndim == 2:
            ax.imshow(self.s[:step], cmap=plt.cm.binary)
        elif self.s.ndim == 3:
            ax.imshow(self.s[step], cmap=plt.cm.binary)
        return fig
