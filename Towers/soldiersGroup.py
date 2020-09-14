from datetime import datetime

from eventNotifier import add_game_tick_events

""""
A group of soldiers
"""
default_soldiers_amount = 5


class SoldiersGroup:
    """
    :parameter team: the team of which the soldiers belongs
    :type team: Player
    :parameter soldiers_amount: the amount of soldiers in the group
    :type soldiers_amount: int
    """

    def __init__(self, team, soldiers_amount=default_soldiers_amount):
        self.team = team
        self.heading = None
        self.soldiers_amount = soldiers_amount
        self.time_started_heading = None
        self.road_used = None

    """
    :parameter tower the tower to which the soldier are heading
    change the destination of the soldier
    """

    def heading(self, tower, road_used):
        self.heading = tower
        self.time_started_heading = datetime.now()
        self.road_used = road_used
        add_game_tick_events(self.add_movement_progress)

    def split(self, amount):
        if amount > self.soldiers_amount:
            raise ValueError("split must have smaller or equal size of soldiers")
        new_group = SoldiersGroup(self.team, self.tower, amount)
        self.soldiers_amount -= amount
        return new_group

    def __add__(self, other):
        if isinstance(other, SoldiersGroup):
            return SoldiersGroup(self.team, self.soldiers_amount + other.soldiers_amount)
        else:
            return SoldiersGroup(self.team, self.soldiers_amount + other)

    def __sub__(self, other):
        if isinstance(other, SoldiersGroup):
            return SoldiersGroup(self.team, self.soldiers_amount - other.soldiers_amount)
        else:
            return SoldiersGroup(self.team, self.soldiers_amount - other)

    def __lt__(self, other):
        if isinstance(other, SoldiersGroup):
            return self.soldiers_amount < other.soldiers_amount
        else:
            return self.soldiers_amount < other

    def __gt__(self, other):
        if isinstance(other, SoldiersGroup):
            return self.soldiers_amount > other.soldiers_amount
        else:
            return self.soldiers_amount > other

    def __le__(self, other):
        if isinstance(other, SoldiersGroup):
            return self.soldiers_amount <= other.soldiers_amount
        else:
            return self.soldiers_amount <= other

    def __ge__(self, other):
        if isinstance(other, SoldiersGroup):
            return self.soldiers_amount >= other.soldiers_amount
        else:
            return self.soldiers_amount >= other

    def __eq__(self, other):
        if isinstance(other, SoldiersGroup):
            return self.soldiers_amount == other.soldiers_amount
        else:
            return self.soldiers_amount == other

    def __abs__(self):
        return SoldiersGroup(self.team, abs(self.soldiers_amount))

    def add_movement_progress(self, current_time):
        if current_time - self.time_started_heading >= self.road_used.movement_duration:
            self._arrive()

    def _arrive(self):
        if self.heading.team == self.team:
            self.heading.supply(self)
        else:
            self.heading.attack(self)

    def _discard(self):
        self.team = None
        self.heading = None
        self.time_heading = None
