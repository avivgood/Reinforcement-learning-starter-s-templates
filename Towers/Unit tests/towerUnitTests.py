import unittest

from eventNotifier import add_game_turn_event
from player import Player
from soldiersGroup import SoldiersGroup
from tower import Tower, levels


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
        soldiers = SoldiersGroup(Player("Blue"), 100)
        opponents = SoldiersGroup(Player("Red"), 20)
        tower = Tower(opponents)
        tower.attack(soldiers)
        self.assertTrue(tower.warriors_group.soldiers_amount == 80 and tower.warriors_group.team == soldiers.team)

    def test_tower_being_supplied(self):
        tower = Tower(SoldiersGroup(Player("Red"), 50), 2)
        soldiers = SoldiersGroup(Player("Red"), 20)
        tower.supply(soldiers)
        self.assertTrue(tower.warriors_group.soldiers_amount == 70)

    def test_tower_updating(self):
        tower = Tower(SoldiersGroup(Player("Blue"), 10), 2)
        add_game_turn_event(lambda: self._test_tower_updating(tower, 10 + levels[2].yield_per_turn))

    def _test_tower_updating(self, tower, expected):
        self.assertTrue(tower.warriors_group.soldiers_amount == expected)




if __name__ == '__main__':
    unittest.main()
