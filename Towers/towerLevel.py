
# TODO: add max capacity


class TowerLevel:
    """
    a level in which a tower can be
    """
    def __init__(self, price, yield_per_turn, construction_time):
        """
            :parameter price: the price for upgrading to this level
            :type price: int
            :parameter yield_per_turn: how many warriors are granted tin this level each level per turn
            :type yield_per_turn: int
            """
        self.price = price
        self.yield_per_turn = yield_per_turn
        self.construction_time = construction_time
