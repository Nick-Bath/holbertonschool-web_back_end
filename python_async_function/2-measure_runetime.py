#!/usr/bin/env python3


"""Module: Concurrent coroutines with async"""


import asyncio
import importlib


module = importlib.import_module("1-concurrent_coroutines")
wait_n = module.wait_n


def measure_time(n: int, max_delay: float) -> float:
    """calculates total time to execution wait_n"""

    exec_times = asyncio.run(wait_n(n, max_delay))
    total_time = 0
    for time in exec_times:
        total_time += time

    return total_time / n
