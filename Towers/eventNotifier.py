import asyncio
from datetime import datetime

sec_per_turn = 3
sec_per_tick = 0.01

game_tick_events = []
game_turn_events = []


def turns_to_secs(turns):
    return turns * sec_per_turn


def start_game():
    asyncio.run(_game_tick())
    asyncio.run(_game_turn())


def add_game_tick_events(function):
    """
    subscribe event to run every tick
    :type function: Union[instancemethod, function]
    """
    game_tick_events.append(function)


def add_game_turn_event(function):
    """
        subscribe event to run every game turn
        :type function: Union[instancemethod, function]
        """
    game_turn_events.append(function)


async def _game_tick():
    while True:
        await asyncio.sleep(sec_per_tick)
        for function in game_tick_events:
            function(datetime.now)


async def _game_turn():
    while True:
        await asyncio.sleep(sec_per_turn)
        for function in game_turn_events:
            function()


asyncio.gather(_game_tick(), _game_turn())
