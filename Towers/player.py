class Player:
    """
    A player in a game. Players attack each others tower's in order to achieve victory
    """
    def __init__(self, color):
        """
        :param color: the color of the player
        """
        self.color = color

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.color == other.color
        else:
            return self.color == other
