
class Road:
    """
    a road connecting two towers. soldiers can only move using roads.
    """
    def __init__(self, tower1, tower2, movement_duration):
        """
        :param tower1: The tower in the first side of the road
        :type tower1: Tower
        :param tower2:  The tower in the second side of the road
        :type tower2: Tower
        :param movement_duration: The time it takes to cross the road
        :type movement_duration: float
        """
        self.tower1 = tower1
        self.tower2 = tower2
        self.movement_duration = movement_duration

    def move_tower1_to_tower2(self, soldiers_amount):
        """
        move warriors from tower1 to tower2 (attacking or supplying, context - dependent)
        :param soldiers_amount:
        :type soldiers_amount:
        """
        soldiers = self.tower1.split(soldiers_amount)
        soldiers.heading(self.tower2)

    def move_tower2_to_tower1(self, soldiers_amount):
        """
                move warriors from tower2 to tower1 (attacking or supplying, context - dependent)
                :param soldiers_amount:
                :type soldiers_amount:
                """
        soldiers = self.tower2.split(soldiers_amount)
        soldiers.heading(self.tower1)
