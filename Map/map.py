""" @file map.py
    @author Sean Duffie
    @brief Abstract wrapper for any references to the current game type
"""

import numpy as np
from typing import List, Literal
import abc


class Map(abc.ABC):
    gametype: Literal['control', 'escort', 'flashpoint', 'hybrid', 'push', 'clash']
    health_packs: List[tuple[int, int]]
    top_down: np.NDArray

    # def __init__(self):
        
