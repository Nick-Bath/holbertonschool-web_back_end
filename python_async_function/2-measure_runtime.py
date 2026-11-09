#!/usr/bin/env python3


"""Module: Concurrent coroutines with async"""


import asyncio
import importlib
import time


module = importlib.import_module("1-concurrent_coroutines")
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """calculates total time to execution wait_n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start

    return total_time / n
