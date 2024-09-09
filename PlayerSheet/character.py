""" @file character.py
    @author Sean Duffie
    @brief Contains the stats from a character
"""
import datetime

from ability import Ability
from ult import Ult


class Character:
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

    def fromsite(self):
        pass

    def timeline(self):
        cycle = {
            # ability: [dmg, dur, cool]
            "recon": [360, 4, 8]
        }
        pass

    def burst_damage(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        pass

    def burst_healing(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        pass

    def average_damage(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        pass

    def average_healing(self, accuracy: float = 0.5, headshots: float = 0.5, splash: int = 1) -> float:
        pass

    def ult_time(self) -> datetime.timedelta:

if __name__ == "__main__":
    pass
