import numpy as np
import matplotlib.pyplot as plt

from .mcs import MCS


class PDE(MCS):
    """PDEs simulation.

    Override this class to customize.

    Attributes:
        max_step: The max step.
        dim: The number of variables.
        dt: The time step.
        dh: Spatial resolution.
        size: Size of grid.
        f: An array of shape (max_step, size, size, dim) representing the states.
        step: The current step.
    """

    def __init__(self, max_step, dim, dt, dh, size):
        super().__init__(max_step)
        self.dim = dim
        self.dt = dt
        self.dh = dh
        self.size = size
        self.f = np.zeros((max_step, size, size, dim))

    def initialize(self):
        """Sets up the initial conditions."""
        x = y = np.arange(0, self.dh * (self.size + 1), self.dh)
        self.xv, self.yv = np.meshgrid(x, y)
        np.random.seed(42)
        self.f[0, ..., 0] = 1 + np.random.uniform(-0.01, 0.01, (self.size, self.size))
        self.f[0, ..., 1] = 1 + np.random.uniform(-0.01, 0.01, (self.size, self.size))

    def update(self, *, F):
        """Updates the states in the next step.

        Args:
            F: A state transition function corresponding to df/dt = F(f,...,x,y,t).
        """
        config = self.f[self.step]
        self.step += 1
        self.f[self.step] = config + F(config) * self.dt

    @staticmethod
    def turing(a, b, c, d, h, k, Du, Dv, dh):
        """Reaction-diffusion equations:

        .. math::
            \partial u/\partial t = a(u-h) + b(v-k) + D_u \Delta u \\
            \partial v/\partial t = c(u-h) + d(v-k) + D_v \Delta v.
        """

        def dfdt(config):
            lap = PDE._laplacian(config, dh)
            u, v = np.moveaxis(config, -1, 0)
            delta_u, delta_v = np.moveaxis(lap, -1, 0)
            du = a * (u - h) + b * (v - k) + Du * delta_u
            dv = c * (u - h) + d * (v - k) + Dv * delta_v
            return np.stack([du, dv], axis=2)

        return dfdt

    @staticmethod
    def _laplacian(u, dh):
        assert u.ndim == 3
        u_r = np.roll(u, -1, axis=1)
        u_l = np.roll(u, 1, axis=1)
        u_u = np.roll(u, -1, axis=0)
        u_d = np.roll(u, 1, axis=0)
        return (u_r + u_l + u_u + u_d - 4 * u) / (dh**2)

    def visualize(self, *, step=-1, indices=None):
        """Visualizes the states of the system using heatmap.

        Args:
            step: The step to plot.
            indices: A list of indices of the states to plot.
            If None, plot all states.
        Returns:
            A list of matplotlib.figure.Figure objects.
        """
        figs = []
        indices = np.arange(self.dim) if indices is None else indices
        for state in indices:
            fig, ax = plt.subplots()
            pcm = ax.pcolormesh(self.xv, self.yv, self.f[step, ..., state], vmin=0, vmax=2)
            ax.set_aspect("equal")
            fig.colorbar(pcm, ax=ax)
            figs.append(fig)
        return figs
