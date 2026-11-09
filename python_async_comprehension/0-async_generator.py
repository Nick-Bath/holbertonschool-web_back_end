#!/usr/bin/env python3


"""Module: Async generator """


import random
import asyncio


async def async_generator() -> float:
    """yields a random number between 0 and 10, tens times, wait 1 sec"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
