# from .worker import LongerBT1003JWorker


# __all__ = ["LongerBT1003JWorker"]
from typing import Literal, Optional

import funcnodes as fn


@fn.NodeDecorator(
    node_id="bt100_3j.set_state",
    name="Pump State",
    description="Set the state of the pump",
    outputs=[{"name": "is pumping", "type": bool}],
)
def set_state(
    rpm: int,
    direction: Literal["CW", "CCW"],
    time: Optional[int] = None,
) -> bool:
    return True


@fn.NodeDecorator(
    node_id="bayezian_optimization",
    name="Bayesian Optimization",
    description="perform bayesian optimization on the input data",
    outputs=[{"name": "result", "type": dict}],
)
def bayes_opt(
    data: dict,
    n_iter: int, # number of iterations
    n_init: int, # number of initial points
    acq_func: Literal["LCB", "EI", "PI"],
    random_state: Optional[int] = None,
) -> dict:
    return {}


NODE_SHELF = fn.Shelf(
    nodes=[set_state, bayes_opt],
    name="BT100 3J",
    description="BT100 3J nodes",
)
