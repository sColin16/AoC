import re
import sys
import argparse
import math

from collections import defaultdict

import sys
sys.path.append('../')

from executor import *
from helpers import *

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = [stoil(list(line)) for line in lines]
    g = Grid(d)

    def is_low(r, c):
        for a, b in g.get_adj4(r, c):
            if g.get(a, b) <= g.get(r, c):
                return False

        return True

    for i in range(len(d)):
        for j in range(len(d[0])):
            if is_low(i, j):
                ans += g.get(i, j) + 1

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = [stoil(list(line)) for line in lines]
    g = Grid(d)

    c = []

    def is_low(r, c):
        for a, b in g.get_adj4(r, c):
            if g.get(a, b) <= g.get(r, c):
                return False

        return True

    for i in range(len(d)):
        for j in range(len(d[0])):
            if is_low(i, j):
                c.append((i, j))
    bs = []

    for a, b in c:
        size = 0
        q = [(a, b)]
        v = set([(a, b)])

        while len(q) > 0:
            size += 1
            i, j = q.pop(0)

            for r, c in g.get_adj4(i, j):
                if (r, c) not in v and g.get(r, c) > g.get(i, j) and g.get(r, c) != 9:
                    q.append((r, c))
                    v.add((r, c))

        bs.append(size)

    bs.sort()
    bs = bs[-3:]

    ans = bs[0] * bs[1] * bs[2]

    return ans

run_solutions(p1, p2)
