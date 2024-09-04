""" @file ability.py
    @author Sean Duffie
    @brief Object class to wrap up ability-related features.
"""

class Ability():
    """ Wrapper for ability data """
    def __init__(self, name: str):
        self.name = name
        self.does_dmg = True
        self.does_healing = False
        self.has_aoe = False
        self.has_cc = False
        self.does_mvmt = False

    def get_burst_dmg(self):
        pass

    def get_avg_dmg(self):
        pass
