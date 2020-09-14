import asyncio
import threading
from datetime import datetime

sec_per_turn = 3

game_tick_events = []
game_turn_events = []


def add_game_tick_events(function):
    game_tick_events.append(function)


def add_game_turn_event(function):
    game_turn_events.append(function)


async def _game_tick():
    while True:
        for funct in game_tick_events:
            funct(datetime.now)


async def _game_turn():
    while True:
        threading.Timer(sec_per_turn, _game_turn).start()
        for function in game_turn_events:
            function()
