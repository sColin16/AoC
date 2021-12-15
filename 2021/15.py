import re
import sys
import argparse
import math

from collections import defaultdict

import sys
sys.path.append('../')

from executor import *
from helpers import *

# This is comically slow for part 2
def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = [stoil(list(line)) for line in lines]

    g = Grid(d)

    ds = create_matrix(len(lines[0]) * 5, len(lines) * 5, 1000000000)
    ds[0][0] = 0
    done = set()

    q = [(0, 0)]
    while len(q) > 0:
        min_d = 100000000000000
        min_c = None
        for e in q:
            if ds[e[0]][e[1]] < min_d:
                min_c = e
                min_d = ds[e[0]][e[1]]

        q.remove(min_c)

        if min_c[0] == len(lines) - 1 and min_c[1] == len(lines[0]) - 1:
            ans = min_d
            break

        for a, b in g.get_adj4(min_c[0], min_c[1]):
            if (a, b) in done or (a, b) in q:
                continue

            if min_d + g.get(b, a) < ds[a][b]:
                ds[a][b] = min_d + g.get(a, b)

            q.append((a, b))

        done.add((min_c[0], min_c[1]))

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = [stoil(list(line)) for line in lines]
    dnew = []

    for line in d:
        row = []
        for i in range(5):
            for element in line:
                row.append((element + i - 1) % 9 + 1)

        dnew.append(row)

    dnew2 = []

    for i in range(5):
        for line in dnew:
            row = []
            for element in line:
                row.append((element + i - 1) % 9 + 1)

            dnew2.append(row)

    d = dnew2

    g = Grid(d)

    ds = create_matrix(len(lines[0]) * 5, len(lines) * 5, 1000000000)
    ds[0][0] = 0
    done = set()

    q = [(0, 0)]
    while len(q) > 0:
        min_d = 100000000000000
        min_c = None
        for e in q:
            if ds[e[0]][e[1]] < min_d:
                min_c = e
                min_d = ds[e[0]][e[1]]

        q.remove(min_c)

        if min_c[0] == len(lines) * 5 - 1 and min_c[1] == len(lines[0]) * 5 - 1:
            ans = min_d
            break

        for a, b in g.get_adj4(min_c[0], min_c[1]):
            if (a, b) in done or (a, b) in q:
                continue

            if min_d + g.get(b, a) < ds[a][b]:
                ds[a][b] = min_d + g.get(a, b)

            q.append((a, b))

        done.add((min_c[0], min_c[1]))
    

    return ans

run_solutions(p1, p2)
