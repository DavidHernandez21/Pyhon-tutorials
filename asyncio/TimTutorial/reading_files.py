import json
import os
from time import perf_counter
from typing import List
from zipfile import ZipFile

import aiofiles

import asyncio

if not os.path.isdir("intents"):
    with ZipFile("intents.zip", "r") as myzip:
        myzip.extractall()

for f in filter(lambda x: x.endswith("_usersays_it.json"), os.listdir("intents")):

    os.remove(f"intents{os.path.sep}{f}")

my_files = []

for f in os.listdir("intents"):
    my_files.append(f"intents{os.path.sep}{f}")

# print(my_files)

# with open(my_files[0], "r") as f:
#  d = json.load(f)


def get_files_sync(file_list: List):
    the_dict = {}
    for fi in file_list:
        with open(fi, "r") as the_file:
            the_dict[fi.split(os.path.sep)[1]] = json.load(the_file)["contexts"]
    return the_dict


async def get_files(file_list: List):
    the_dict = {}
    # names = []
    tasks = []
    for fi in file_list:
        # names.append(fi)
        async with aiofiles.open(fi, mode="r") as aio_file:

            the_dict[fi.split(os.path.sep)[1]] = json.loads(await aio_file.read())[
                "contexts"
            ]
            # tasks.append(asyncio.create_task(aio_file.read()))

            # parsing = await asyncio.gather(*tasks)

    # for j, fi in zip(tasks, names):
    #    the_dict[fi.split(os.path.sep)[1]] = json.loads(j)["contexts"]

    return the_dict


async def main():

    task1 = asyncio.create_task(get_files(my_files))

    return await task1


if __name__ == "__main__":
    t0 = perf_counter()
    dicty = asyncio.run(main())
    # dicty = get_files_sync(my_files)
    print(f"function took {perf_counter() - t0:.05f} s")
    print(dicty)
