from eventNotifier import add_game_turn_event
from soldiersGroup import SoldiersGroup
from towerLevel import TowerLevel

levels = {1: TowerLevel(0, 5, 0), 2: TowerLevel(10, 8, 2), 3: TowerLevel(15, 11, 3)}

"""
represents a tower in the game. towers holds warriors. The objective his to control as many towers as possible
"""


class Tower:
    """
    :parameter warriors_group: the group of warriors that currently are found in the tower
    :type warriors_group: SoldiersGroup
    :parameter level: the level of the tower. Higher levels yields more soldiers per turn
    :type level: int
    """

    def __init__(self, warriors_group, level):
        self.warriors_group = warriors_group
        self.level = level
        self.update_time = 0
        self.waiting_for_update = False
        add_game_turn_event(self._update)

    """
    :parameter tower the tower to attack by the current tower
    :parameter warriors_amount the amount of warriors attacking
    :returns True if the attack is valid, otherwise false
    attack a connected tower from a different team using soldiers from the current tower
    """

    def attack(self, warriors_group):
        if warriors_group.team == self.warriors_group.team:
            self.warriors_group -= warriors_group
            if self.warriors_group < 0:
                self.warriors_group = abs(self.warriors_group)
                self.warriors_group.team = warriors_group.team
            return True
        return False

    """
    :parameter tower to supply
    :parameter warriors_amount amount of warriors to supply
    supply a tower from the same team with warriors
    """

    def supply(self, warriors_group):
        if warriors_group.team == self.team:
            self.warriors_group += warriors_group
            return True
        return False

    """
    update the tower in the next turn. updated towers yields more warriors per turn
    """

    def apply_for_update(self):
        if not max(levels) == self.level and self.warriors_group >= levels[self.level + 1].price and \
                self.update_time == 0 and not self.waiting_for_update:
            self.waiting_for_update = True
            return True
        return False

    def _update(self):
        if self.waiting_for_update:
            self.warriors_group -= levels[self.level + 1].price
            self.update_time = levels[self.level + 1].construction_time
            self.waiting_for_update = False

    """
    make changes to warriors amount and updates when a turn starts
    """

    def turn_result(self):
        if self.update_time == 1:
            self.level += 1
        if not self.update_time == 0:
            self.update_time -= 1
        if self.waiting_for_update:
            self._update()
        self.warriors_group += levels[self.level].yield_per_turn

    # TODO disallow split when updating

    def split(self, warriors_amount):
        return self.warriors_group.split(warriors_amount)

