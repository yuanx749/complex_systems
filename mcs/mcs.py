from abc import ABC, abstractmethod


class MCS(ABC):
    """Complex system simulation.

    Attributes:
        max_step: The max step.
        step: The current step.
    """

    @abstractmethod
    def __init__(self, max_step):
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

    def simulate(self, stop_step=None, **kwargs):
        """Simulates the system till stop_step.

        Args:
            stop_step: If None, stops at max_step.
            kwagrs: Parameters passed to update().
        """
        stop_step = self.max_step if stop_step is None else stop_step
        while self.step < stop_step - 1:
            self.update(**kwargs)
