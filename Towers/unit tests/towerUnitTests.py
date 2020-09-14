import unittest

from player import Player
from soldiersGroup import SoldiersGroup
from tower import Tower


class TestTower(unittest.TestCase):
    def test_tower_creation(self):
        new_tower = Tower(SoldiersGroup(Player('Blue')))
        print("done")
        self.assertTrue(new_tower.waiting_for_update is False and new_tower.update_time == 0 and new_tower.level == 1
                        and new_tower.warriors_group == SoldiersGroup(Player('Blue')))

    def test_tower_being_attacked_with_insufficient_troops(self):
        soldiers = SoldiersGroup("Blue", 50)
        opponents = SoldiersGroup("Red", 70)
        tower = Tower(opponents)
        tower.attack(soldiers)
        self.assertTrue(tower.warriors_group == 20 and tower.warriors_group.team == opponents)

    def test_tower_being_attacked_with_sufficient_troops(self):
        soldiers = SoldiersGroup("Blue", 50)
        opponents = SoldiersGroup("Red", 70)
        tower = Tower(opponents)
        tower.attack(soldiers)
        self.assertTrue(tower.warriors_group.soldiers_amount == 20)


if __name__ == '__main__':
    unittest.main()
