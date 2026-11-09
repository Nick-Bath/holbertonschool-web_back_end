#!/usr/bin/env python3


"""Module: Basic Async Syntax"""


import asyncio
import random
import importlib

module = importlib.import_module("0-basic_async_syntax")
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """spawns wait_random n times with max_delay, returns delay list ASC"""

    delay_list = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay_list.append(await task)

    return delay_list
