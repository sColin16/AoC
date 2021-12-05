import re
import sys
import argparse
import math

import sys
sys.path.append('../')

from executor import *
from helpers import *

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    SIZE = 1000

    coords = []
    for line in lines:
        c = get_regex_groups("(\d+),(\d+) -> (\d+),(\d+)", line)

        coords.append([int(num) for num in c])

    grid = create_matrix(SIZE, SIZE, 0)

    for coord in coords:
        x1, y1, x2, y2 = coord

        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2:
            for y in drange(y1, y2):
                grid[y][x1] += 1

        elif y1 == y2:
            for x in drange(x1, x2):
                grid[y1][x] += 1

    for line in grid:
        for element in line:
            if element >= 2:
                ans += 1

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    SIZE = 1000

    coords = []
    for line in lines:
        c = get_regex_groups("(\d+),(\d+) -> (\d+),(\d+)", line)

        coords.append([int(num) for num in c])

    grid = create_matrix(SIZE, SIZE, 0)

    for coord in coords:
        x1, y1, x2, y2 = coord

        if x1 == x2:
            for y in drange(y1, y2):
                grid[y][x1] += 1

        elif y1 == y2:
            for x in drange(x1, x2):
                grid[y1][x] += 1

        else:
            seq1 = list(drange(x1, x2))
            seq2 = list(drange(y1, y2))

            for i in range(len(seq1)):
                grid[seq2[i]][seq1[i]] += 1

    for line in grid:
        for element in line:
            if element >= 2:
                ans += 1

    return ans

run_solutions(p1, p2)
