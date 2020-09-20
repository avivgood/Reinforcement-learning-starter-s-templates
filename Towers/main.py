import asyncio

from Enums.gameLevel import GameLevel
from eventNotifier import _game_tick, _game_turn
from map import Map


async def main():
    map_ = Map(GameLevel.EASY.value)


async def driver():
    await asyncio.gather(_game_tick(), _game_turn(), main())

if __name__ == '__main__':
    asyncio.run(driver())
