from player import Player


class Map:
    def __init__(self, roads):
        """

        :param roads: all the roads that connect two towers
        :type roads: set

        """
        self.roads = roads

    def move(self, tower1, tower2):
        for road in self.roads:
            if road.tower1 == tower1 and road.tower2 == tower2:
                road.move_tower1_to_tower2()
            if road.tower1 == tower2 and road.tower2 == tower1:
                road.move_tower2_to_tower1()

    def winner(self):
        players_with_towers = set()
        for road in self.roads:
            players_with_towers.add(road.tower1.team)
            players_with_towers.add(road.tower2.team)
