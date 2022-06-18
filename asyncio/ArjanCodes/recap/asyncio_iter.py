import asyncio
from random import randint
from typing import AsyncIterable

from req_http import http_get

# The highest Pokemon id
MAX_POKEMON = 898


async def get_random_pokemon_name() -> str:
    # pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{randint(1, MAX_POKEMON)}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        yield await get_random_pokemon_name()


async def main():

    # retrieve the next 10 pokemon names
    # async for name in next_pokemon(10):
    #     print(name)

    # asynchronous list comprehensions
    # this is way faster than the previous version
    names = [name async for name in next_pokemon(10)]
    print(names)


if __name__ == "__main__":
    asyncio.run(main()) 