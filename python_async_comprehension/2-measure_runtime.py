#!/usr/bin/env python3


"""Measures the runtime of concurrent async generators """


import random
import asyncio
from typing import List
import time
comprehen = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs four async comprhensions concurrently and returns the total time"""
    start = time.perf_counter()
    await asyncio.gather(comprehen(), comprehen(), comprehen(), comprehen())
    total_time = time.perf_counter() - start

    return total_time
