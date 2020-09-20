from player import Player


class Map:
    def __init__(self, roads):
        """
        :param roads: all the roads that connect two towers
        :type roads: set
        """
        self.roads = roads

    def move(self, tower1, tower2):
        """
        :param tower1: the source tower for the warriors
        :type tower1: Tower
        :param tower2: the destination tower for the warriors
        :type tower2: Tower
        """
        for road in self.roads:
            if road.tower1 == tower1 and road.tower2 == tower2:
                road.move_tower1_to_tower2()
            if road.tower1 == tower2 and road.tower2 == tower1:
                road.move_tower2_to_tower1()

    def winner(self):
        """
        checks who the winner, if any yet, of the game
        :return: teh winner, or None if there is no wining player
        :rtype: Player
        """
        players_with_towers = set()
        for road in self.roads:
            players_with_towers.add(road.tower1.team)
            players_with_towers.add(road.tower2.team)
        if len(players_with_towers) == 1:
            return next(iter(players_with_towers))
        elif len(players_with_towers) == 2:
            teams = iter(players_with_towers)
            first_team = next(teams)
            second_team = next(teams)
            if first_team == "Gray":
                return second_team
            elif second_team == "Gray":
                return first_team
            else:
                return None
        else:
            return None
