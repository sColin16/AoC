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
        a, b = line.split(' -> ')
        x1, y1 = a.split(',')
        x2, y2 = b.split(',')

        coords.append((int(x1), int(y1), int(x2), int(y2)))

    grid = create_matrix(SIZE, SIZE, 0)

    for coord in coords:
        x1, y1, x2, y2 = coord

        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2:
            t1 = min(y1, y2)
            t2 = max(y1, y2)

            for y in range(t1, t2+1):
                grid[y][x1] += 1

        elif y1 == y2:
            t1 = min(x1, x2)
            t2 = max(x1, x2)
            for x in range(t1, t2+1):
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
        a, b = line.split(' -> ')
        x1, y1 = a.split(',')
        x2, y2 = b.split(',')

        coords.append((int(x1), int(y1), int(x2), int(y2)))

    grid = create_matrix(SIZE, SIZE, 0)

    for coord in coords:
        x1, y1, x2, y2 = coord

        if x1 == x2:
            t1 = min(y1, y2)
            t2 = max(y1, y2)

            for y in range(t1, t2+1):
                grid[y][x1] += 1

        elif y1 == y2:
            t1 = min(x1, x2)
            t2 = max(x1, x2)
            for x in range(t1, t2+1):
                grid[y1][x] += 1

        else:
            if x1 < x2:
                seq1 = list(range(x1, x2+1))
            else:
                seq1 = list(range(x1, x2-1, -1))

            if y1 < y2:
                seq2 = list(range(y1, y2+1))
            else:
                seq2 = list(range(y1, y2-1, -1))

            for i in range(len(seq1)):
                grid[seq2[i]][seq1[i]] += 1

    for line in grid:
        for element in line:
            if element >= 2:
                ans += 1

    return ans

run_solutions(p1, p2)
