__version__ = "0.3.0"

from .de import DE
from .ode import ODE
from .ca import CA
from .pde import PDE
from .net import Net

__all__ = ["DE", "ODE", "CA", "PDE", "Net"]
