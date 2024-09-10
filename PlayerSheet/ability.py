""" @file ability.py
    @author Sean Duffie
    @brief Object class to wrap up ability-related features.
"""
import abc


class Ability(abc.ABC):
    """ Wrapper for ability data """
    def __init__(self, name: str):
        self.name = name
        self.does_dmg = True
        self.does_healing = False
        self.has_aoe = False
        self.has_cc = False
        self.does_mvmt = False

        self.duration = 2
        self.cooldown = 8

    @abc.abstractmethod
    def get_burst_dmg(self, acc: float = 0.5, head: float = 0.5, splash: int = 1):
        """ 
        """
        pass

    @abc.abstractmethod
    def get_avg_dmg(self, acc: float = 0.5, head: float = 0.5, splash: int = 1):
        pass

    @abc.abstractmethod
    def get_burst_heal(self, acc: float = 0.5, head: float = 0.5, splash: int = 1):
        pass

    @abc.abstractmethod
    def get_avg_heal(self, acc: float = 0.5, head: float = 0.5, splash: int = 1):
        pass
