#!/usr/bin/env python3


"""Module: Async generator """


import random
import asyncio
from typing import List
generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects and returns 10 numbers from a generator"""
    numbers = []

    async for number in generator():
        numbers.append(number)
    return numbers
