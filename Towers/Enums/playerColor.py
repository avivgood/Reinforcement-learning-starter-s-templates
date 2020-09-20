from enum import Enum

from player import Player


class PlayerColor(Enum):
    RED = Player('Red')
    GRAY = Player('Gray')
    BLUE = Player('Blue')
