#!/usr/bin/env python3


"""Module: Concurrent coroutines with async"""


import asyncio
import importlib
import time


module = importlib.import_module("0-basic_async_syntax")
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a task to be executed"""

    task = asyncio.create_task(wait_random(max_delay))

    return task
