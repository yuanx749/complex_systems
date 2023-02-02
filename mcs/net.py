import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from .mcs import MCS


class Net(MCS):
    """Dynamical networks simulation.

    Override this class to customize.

    Attributes:
        max_step: The max step.
        graphs: A list of networkx.Graph objects.
    """

    def __init__(self, max_step):
        super().__init__(max_step)
        self.graphs = []

    def initialize(self):
        """Sets up the initial network."""
        g = nx.karate_club_graph()
        np.random.seed(42)
        for i in g.nodes:
            g.nodes[i]["state"] = np.random.random()
        self.graphs.append(g)

    def update(self, **kwargs):
        """Updates the states in the next step."""
        self.coupled_oscillators(**kwargs)

    def coupled_oscillators(self, a, b, dt):
        """Linearly coupled dynamical nodes:

        .. math::
            d\theta_i/dt = b\theta_i + a\sum_{j\in N_i}(\theta_j-\theta_i).
        """
        g = self.graphs[-1]
        g_next = g.copy()
        for i in g.nodes:
            theta_i = g.nodes[i]["state"]
            sum_ni = sum(g.nodes[j]["state"] - theta_i for j in g.neighbors(i))
            g_next.nodes[i]["state"] = theta_i + (b * theta_i + a * sum_ni) * dt
        self.graphs.append(g_next)
        self.step += 1

    def visualize(self, *, step=-1):
        """Visualizes the states of the network.

        Args:
            step: The step to plot.
        Returns:
            A matplotlib.figure.Figure object.
        """
        g = self.graphs[step]
        fig, ax = plt.subplots()
        nx.draw(
            g,
            pos=nx.spring_layout(g, seed=42),
            ax=ax,
            node_color=[np.sin(g.nodes[i]["state"]) for i in g.nodes],
            cmap=plt.cm.hsv,
            vmin=-1,
            vmax=1,
        )
        return fig
