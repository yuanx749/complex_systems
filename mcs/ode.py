from .mcs import *


class ODE(MCS):
    """ODEs simulation.

    Attributes:
        max_step: The max step.
        dim: The number of variables.
        dt: The time step.
        x: An `~numpy.ndarray` representing the states of shape (max_step, dim).
        t: An `~numpy.ndarray` of length max_step representing time.
        step: The current step.
    """

    def __init__(self, max_step: int, dim: int, dt: float):
        super().__init__(max_step)
        self.dim = dim
        self.dt = dt
        self.x = np.zeros((max_step, dim))
        self.t = np.zeros(max_step)

    def initialize(self, *, x0: List[float] = None):
        """Sets up the initial values for the state variables.

        Args:
            x0: A list of initial states.
        """
        if x0 is None:
            x0 = [0] * len(self.dim)
        assert len(x0) == self.dim
        self.x[0] = x0
        self.t[0] = 0

    def update(self, *, f: Callable = None):
        """Updates the states in the next step.

        Args:
            f: A function, :math:`dx/dt = f(x)`.
        """
        if f is None:
            f = self._identity
        x = self.x[self.step]
        dxdt = f(x)
        self.step += 1
        self.x[self.step] = x + dxdt * self.dt
        self.t[self.step] = self.t[self.step - 1] + self.dt

    @staticmethod
    def lv(a, b, c, d):
        """Returns Lotka-Volterra equations."""

        def dxdt(states):
            x, y = states
            dx = a * x - b * x * y
            dy = d * x * y - c * y
            return np.array([dx, dy])

        return dxdt

    def visualize(self, *, step: int = -1, indices: List[int] = None):
        """Visualizes the time series of the system.

        Args:
            step: The step to plot.
            indices: A list of indices of the states to plot.
                If `None`, plot all states.
        Returns:
            A `matplotlib.figure.Figure` object.
        """
        fig, ax = plt.subplots()
        indices = np.arange(self.dim) if indices is None else indices
        for state in indices:
            ax.plot(self.t[:step], self.x[:step, state])
        return fig
