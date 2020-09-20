from enum import Enum

from Enums.playerColor import PlayerColor
from eventNotifier import turns_to_secs
from road import Road
from soldiersGroup import SoldiersGroup
from tower import Tower

BlueTower1 = Tower(1, SoldiersGroup(PlayerColor.BLUE))
BlueTower2 = Tower(2, SoldiersGroup(PlayerColor.BLUE))
BlueTower3 = Tower(3, SoldiersGroup(PlayerColor.BLUE))
BlueTower4 = Tower(4, SoldiersGroup(PlayerColor.BLUE))
BlueTower5 = Tower(5, SoldiersGroup(PlayerColor.BLUE))

GrayTower1 = Tower(6, SoldiersGroup(PlayerColor.GRAY), 2)
GrayTower2 = Tower(7, SoldiersGroup(PlayerColor.GRAY), 2)
GrayTower3 = Tower(8, SoldiersGroup(PlayerColor.GRAY), 2)

RedTower1 = Tower(9, SoldiersGroup(PlayerColor.RED))
RedTower2 = Tower(10, SoldiersGroup(PlayerColor.RED))
RedTower3 = Tower(11, SoldiersGroup(PlayerColor.RED))
RedTower4 = Tower(12, SoldiersGroup(PlayerColor.RED))
RedTower5 = Tower(13, SoldiersGroup(PlayerColor.RED))


class GameLevel(Enum):

    EASY = {Road(BlueTower1, BlueTower2, turns_to_secs(2)), Road(BlueTower2, BlueTower3, turns_to_secs(2)),
            Road(GrayTower1, BlueTower2, turns_to_secs(3)), Road(GrayTower1, BlueTower1, turns_to_secs(3)),
            Road(GrayTower2, BlueTower2, turns_to_secs(3)), Road(GrayTower2, BlueTower3, turns_to_secs(3)),
            Road(RedTower1, RedTower2, turns_to_secs(2)), Road(GrayTower1, RedTower2, turns_to_secs(3)),
            Road(GrayTower1, RedTower1, turns_to_secs(3)), Road(GrayTower1, GrayTower2, turns_to_secs(1))}
    
    MEDIUM = {Road(BlueTower1, BlueTower2, turns_to_secs(2)), Road(BlueTower2, BlueTower3, turns_to_secs(2)),
              Road(GrayTower1, BlueTower2, turns_to_secs(3)), Road(GrayTower1, BlueTower1, turns_to_secs(3)),
              Road(GrayTower1, GrayTower2, turns_to_secs(1)),
              Road(RedTower1, RedTower2, turns_to_secs(2)), Road(RedTower2, RedTower3, turns_to_secs(2)),
              Road(GrayTower1, RedTower2, turns_to_secs(3)), Road(GrayTower1, RedTower1, turns_to_secs(3))}
    
    HARD = {Road(RedTower1, RedTower2, turns_to_secs(2)), Road(RedTower2, RedTower3, turns_to_secs(2)),
            Road(GrayTower1, RedTower2, turns_to_secs(3)), Road(GrayTower1, RedTower1, turns_to_secs(3)),
            Road(GrayTower2, RedTower2, turns_to_secs(3)), Road(GrayTower2, RedTower3, turns_to_secs(3)),
            Road(BlueTower1, BlueTower2, turns_to_secs(2)), Road(GrayTower1, BlueTower2, turns_to_secs(3)),
            Road(GrayTower1, BlueTower1, turns_to_secs(3)), Road(GrayTower1, GrayTower2, turns_to_secs(1))}
