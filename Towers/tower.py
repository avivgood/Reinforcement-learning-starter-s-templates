from eventNotifier import add_game_turn_event
from exceptions.levelError import LevelDosentExistsError
from exceptions.towerErrors import TowerIDAlreadyExistsError, TowerOperationPreformedOnTheWrongTeamError, \
    InvalidTowerOperationError
from soldiersGroup import SoldiersGroup
from towerLevel import TowerLevel

levels = {1: TowerLevel(0, 5, 0), 2: TowerLevel(10, 8, 2), 3: TowerLevel(15, 11, 3)}
tower_ids = set()


class Tower:
    """
    represents a tower in the game. towers holds warriors. The objective his to control as many towers as possible
    """
    def __init__(self, tower_no, warriors_group, level=1):

        """
        :parameter tower_no: the id of the tower
        :type tower_no: int
        :parameter warriors_group: the group of warriors that currently are found in the tower
        :type warriors_group: SoldiersGroup
        :parameter level: the level of the tower. Higher levels yields more soldiers per turn
        :type level: int
        """
        if tower_no in tower_ids:
            raise TowerIDAlreadyExistsError()
        if level not in levels:
            raise LevelDosentExistsError()
        self.warriors_group = warriors_group
        self.level = level
        self.update_time = 0
        self.waiting_for_update = False
        self.tower_no = tower_no
        add_game_turn_event(self._turn_result)

    def attack(self, warriors_group):

        """
        :parameter warriors_group: the group of warriors attacking
        :type warriors_group: SoldiersGroup
        attack a connected tower from a different team using soldiers from the current tower
        """
        if warriors_group.team == self.warriors_group.team:
            raise TowerOperationPreformedOnTheWrongTeamError()
        if self.update_time != 0:
            raise InvalidTowerOperationError("Tower is updating")
        self.warriors_group -= warriors_group
        if self.warriors_group < 0:
            self.warriors_group = abs(self.warriors_group)
            self.warriors_group.team = warriors_group.team
            self.level = 1

    def supply(self, warriors_group):

        """
           :parameter warriors_group: the group of warriors to supply
           :type warriors_group: SoldiersGroup
           supply a tower from the same team with warriors
           """
        if not warriors_group.team == self.warriors_group.team:
            raise TowerOperationPreformedOnTheWrongTeamError()
        self.warriors_group += warriors_group

    def apply_for_update(self):

        """
        update the tower in the next turn. updated towers yields more warriors per turn
        """
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

    def _turn_result(self):
        """
          make changes to warriors amount and updates when a turn starts
        """

        if self.update_time == 1:
            self.level += 1
        if not self.update_time == 0:
            self.update_time -= 1
        if self.waiting_for_update:
            self._update()
        self.warriors_group += levels[self.level].yield_per_turn

    def split(self, warriors_amount):
        """
        splits a group of warriors away from the tower
        :param warriors_amount: the amount of warriors in the new group
        :type warriors_amount:
        :return: the warriors that are split away from the tower
        :rtype: SoldiersGroup
        """
        if self.update_time != 0:
            raise
        return self.warriors_group.split(warriors_amount)

    def __str__(self):
        result = '''
        |||||||
         |||||
         |||||
         ||{}||
        '''.format(str(self.warriors_group))
        return result
