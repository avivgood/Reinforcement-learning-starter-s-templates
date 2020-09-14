import unittest

from player import Player
from soldiersGroup import SoldiersGroup
from tower import Tower


class TestTower(unittest.TestCase):
    def test_assert_tower_creation(self):
        new_tower = Tower(SoldiersGroup(Player('Blue'), ))


if __name__ == '__main__':
    unittest.main()
