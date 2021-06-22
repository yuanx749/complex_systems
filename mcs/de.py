import numpy as np
import matplotlib.pyplot as plt

from .mcs import MCS

class DE(MCS):
    """
    Difference equations simulation.
    Attributes:
        max_step: The max step.
        dim: The number of variables.
        x: An array representing the states of shape (max_step, dim).
        step: The current step.
    """
    def __init__(self, max_step, dim):
        super().__init__(max_step)
        self.dim = dim
        self.x = np.zeros((max_step, dim))

    def initialize(self, x0):
        """
        Sets up the initial values for the state variables.
        Args:
            x0: A list of initial states.
        """
        self.x[0] = x0

    def update(self, f):
        """
        Updates the states in the next step.
        Args:
            f: A function, x_t = f(x_{t-1}).
        """
        x = self.x[self.step]
        self.step += 1
        self.x[self.step] = np.array(f(x))

    def visualize(self, step=-1, indices=None):
        """
        Visualizes the series of states of the system.
        Args:
            step: The step to plot.
            states: A list of indices of the states to plot.
            If None, plot all states.
        Returns:
            A matplotlib.figure.Figure object.
        """
        fig, ax = plt.subplots()
        indices = np.arange(self.dim) if indices is None else indices
        for state in indices:
            ax.plot(self.x[:step, state])
        return fig
