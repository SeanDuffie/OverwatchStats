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
    team1_spawns: List[tuple[int, int]]
    team2_spawns: List[tuple[int, int]]
    checkpoints : List[tuple[int, int]]

    # def __init__(self):
        
