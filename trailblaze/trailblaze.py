"""
Usage
=====

import time
from trailblaze import blaze

for i in range(10):
    blaze('a')
    time.sleep(0.2)
    blaze('b')
    time.sleep(0.1)
"""

import time
from collections import defaultdict

from blessed import Terminal

_t = Terminal()

__all__ = ["Trail", "blaze"]


class _RunningMean:
    def __init__(self):
        self.mean = 0.0
        self.count = 0

    def update(self, new_val: int):
        self.mean = self.mean / (self.count + 1) * self.count + new_val / (
            self.count + 1
        )
        self.count += 1


class Trail:
    def __init__(self, decimals=2):
        self.blazes: dict[str, _RunningMean] = defaultdict(lambda: _RunningMean())
        self.prev_label = None
        self.prev_time = time.time_ns()
        self.lines_printed_prev_time = 0
        self.decimals = decimals

    def blaze(self, name: str):
        curr_time = time.time_ns()
        if self.prev_label is not None:
            self.blazes[self.prev_label].update(curr_time - self.prev_time)
            self.__show()
        self.prev_label = name
        self.prev_time = time.time_ns()  # avoid counting overhead time.

    def __show(self):
        if self.lines_printed_prev_time:
            print(_t.move_up(self.lines_printed_prev_time + 1))
        lines_printed = 0
        for start in self.blazes:
            mean = round(self.blazes[start].mean / 1e9, self.decimals)
            n = self.blazes[start].count
            print(f"{start}: {mean}s (n={n})")
            lines_printed += 1
        self.lines_printed_prev_time = lines_printed


_trail = Trail()

blaze = _trail.blaze
