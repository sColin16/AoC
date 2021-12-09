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

    c = []
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            if i > 0:
                if int(lines[i - 1][j]) <= int(num):
                    continue

            if i < len(lines) - 1:
                if int(lines[i + 1][j]) <= int(num):
                    continue

            if j > 0:
                if int(lines[i][j - 1]) <= int(num):
                    continue

            if j < len(line) - 1:
                if int(lines[i][j + 1]) <= int(num):
                    continue

            c.append((i, j))

    for a, b in c:
        ans += int(lines[a][b]) + 1

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    c = []
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            if i > 0:
                if int(lines[i - 1][j]) <= int(num):
                    continue

            if i < len(lines) - 1:
                if int(lines[i + 1][j]) <= int(num):
                    continue

            if j > 0:
                if int(lines[i][j - 1]) <= int(num):
                    continue

            if j < len(line) - 1:
                if int(lines[i][j + 1]) <= int(num):
                    continue

            c.append((i, j))

    for a, b in c:
        ans += int(lines[a][b]) + 1

    ans = 0

    bs = []

    for a, b in c:
        q = [(a, b)]
        v = set()
        v.add((a, b))
        size = 0

        while len(q) > 0:
            size += 1
            i, j = q.pop(0)

            if i > 0 and (i - 1, j) not in v and int(lines[i - 1][j]) > int(lines[i][j]) and int(lines[i - 1][j]) != 9:
                q.append((i - 1, j))
                v.add((i - 1, j))

            if i < len(lines) - 1 and (i + 1, j) not in v and int(lines[i + 1][j]) > int(lines[i][j]) and int(lines[i + 1][j]) != 9:
                q.append((i + 1, j))
                v.add((i + 1, j))

            if j > 0 and (i, j - 1) not in v and int(lines[i][j - 1]) > int(lines[i][j]) and int(lines[i][j - 1]) != 9:
                q.append((i, j - 1))
                v.add((i, j - 1))

            if j < len(lines[0]) - 1 and (i, j + 1) not in v and int(lines[i][j + 1]) > int(lines[i][j]) and int(lines[i][j + 1]) != 9:
                q.append((i, j + 1))
                v.add((i, j + 1))

        bs.append(size)

    bs.sort()
    bs = bs[-3:]

    ans = bs[0] * bs[1] * bs[2]

    return ans

run_solutions(p1, p2)
