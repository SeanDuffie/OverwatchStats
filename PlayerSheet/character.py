""" @file character.py
    @author Sean Duffie
    @brief Contains the stats from a character
"""
import abc
import datetime
from typing import List

from ability import Ability
from ult import Ult


class Character(abc.ABC):
    """_summary_

    Args:
        abc (_type_): _description_
    """
    a_list: List[Ability]
    ult: Ult

    def __init__(self, name):
        self.name = name
        self.cls = "Support"

        self.health = 250
        self.armor = 0
        self.shields = 0
        self.total_health = self.health + self.armor + self.shields
        self.effective_health = self.health + self.armor * 1.3 + self.shields

        self.ult_cost = 2900

        #Primary
        #Secondary
        #Shift
        #E
        #Ult

    @abc.abstractmethod
    def fromsite(self):
        """_summary_
        """
        pass

    @abc.abstractmethod
    def timeline(self):
        """_summary_
        """
        cycle = {
            # ability: [dmg, dur, cool]
            "recon": [360, 4, 8]
        }
        pass

    def burst_damage(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        """ How much damage can they do over a short period of time?

        FIXME: Should healing and damage be combined for burst/avg? (Return Tuple instead)

        Args:
            accuracy (float, optional): What percent of shots do you hit?. Defaults to 0.5.
            headshots (float, optional): What percent of hits are headshots?. Defaults to 0.5.
            splash (int, optional): How many people are being hit?. Defaults to 1.

        Returns:
            float: Damage that is output over a short period of time (no reloads/cooldowns)
        """
        pass

    def burst_healing(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        """ How much healing can they do over a short period of time?

        FIXME: Should healing and damage be combined for burst/avg? (Return Tuple instead)

        Args:
            accuracy (float, optional): What percent of shots do you hit?. Defaults to 0.5.
            headshots (float, optional): What percent of hits are headshots?. Defaults to 0.5.
            splash (int, optional): How many people are being hit?. Defaults to 1.

        Returns:
            float: Healing that is output over a short period of time (no reloads/cooldowns)
        """
        pass

    def average_damage(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        """ How much damage can they do over a short period of time?

        FIXME: Should healing and damage be combined for burst/avg? (Return Tuple instead)

        Args:
            accuracy (float, optional): What percent of shots do you hit?. Defaults to 0.5.
            headshots (float, optional): What percent of hits are headshots?. Defaults to 0.5.
            splash (int, optional): How many people are being hit?. Defaults to 1.

        Returns:
            float: Damage that is output over a short period of time (no reloads/cooldowns)
        """
        pass

    def average_healing(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        """ How much damage can they do over a short period of time?

        FIXME: Should healing and damage be combined for burst/avg? (Return Tuple instead)

        Args:
            accuracy (float, optional): What percent of shots do you hit?. Defaults to 0.5.
            headshots (float, optional): What percent of hits are headshots?. Defaults to 0.5.
            splash (int, optional): How many people are being hit?. Defaults to 1.

        Returns:
            float: Damage that is output over a short period of time (no reloads/cooldowns)
        """
        pass

    def ult_time(self) -> datetime.timedelta:
        pass

if __name__ == "__main__":
    pass
