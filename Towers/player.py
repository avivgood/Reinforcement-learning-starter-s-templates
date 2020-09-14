class Player:
    def __init__(self, color):
        """
        :param color: the color of the player
        """
        self.color = color

    def __eq__(self, other):
        return self.color == other.color
