import numpy as np
import matplotlib.pyplot as plt

from .mcs import MCS

class ODE(MCS):
    """
    ODEs simulation.
    Attributes:
        max_step: The max step.
        dim: The number of variables.
        dt: The time step.
        x: An array representing the states of shape (max_step, dim).
        t: An array of length max_step representing time.
        step: The current step.
    """
    def __init__(self, max_step, dim, dt):
        super().__init__(max_step)
        self.dim = dim
        self.dt = dt
        self.x = np.zeros((max_step, dim))
        self.t = np.zeros(max_step)

    def initialize(self, x0):
        """
        Sets up the initial values for the state variables.
        Args:
            x0: A list of initial states.
        """
        self.x[0] = x0
        self.t[0] = 0

    def update(self, f):
        """
        Updates the states in the next step.
        Args:
            f: A function, dx/dt = f(x).
        """
        x = self.x[self.step]
        dxdt = f(x)
        self.step += 1
        self.x[self.step] = x + dxdt*self.dt
        self.t[self.step] = self.t[self.step - 1] + self.dt

    @staticmethod
    def lv(a, b, c, d):
        def dxdt(states):
            x, y = states
            dx = a*x - b*x*y
            dy = d*x*y - c*y
            return np.array([dx, dy])
        return dxdt

    def visualize(self, step=-1, indices=None):
        """
        Visualizes the time series of the system.
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
            ax.plot(self.t[:step], self.x[:step, state])
        return fig
