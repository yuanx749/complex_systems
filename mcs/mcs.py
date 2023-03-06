from abc import ABC, abstractmethod
from typing import Callable, List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy import signal


class MCS(ABC):
    """Complex system simulation.

    Attributes:
        max_step: The max step.
        step: The current step.
    """

    @abstractmethod
    def __init__(self, max_step: int):
        self.max_step = max_step
        self.step = 0

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def visualize(self):
        pass

    def simulate(self, stop_step: int = None, **kwargs):
        """Simulates the system till `stop_step`.

        Args:
            stop_step: If `None`, stops at :attr:`max_step`.
            **kwargs: Parameters passed to :meth:`update`.
        """
        stop_step = self.max_step if stop_step is None else stop_step
        while self.step < stop_step - 1:
            self.update(**kwargs)

    @staticmethod
    def _identity(x):
        return x
