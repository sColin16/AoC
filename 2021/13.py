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

    s = set()

    for line in sections[0]:
        a, b = line.split(',')
        s.add((int(a), int(b)))

    axis, c = get_regex_groups(r'([xy])=(\d+)', sections[1][0])
    c = int(c)

    new = set()
    for key in s:
        x, y = key

        if axis == 'x':
            if x < c:
                new.add((x, y))

            else:
                new.add((2 * c - x, y))

        else:
            if y < c:
                new.add((x, y))

            else:
                new.add((x, 2 * c-y))

    ans = len(new)

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    s = set()

    for line in sections[0]:
        a, b = line.split(',')
        s.add((int(a), int(b)))

    for i in range(len(sections[1])):
        axis, c = get_regex_groups(r'([xy])=(\d+)', sections[1][i])
        c = int(c)

        new = set()
        for key in s:
            x, y = key

            if axis == 'x':
                if x < c:
                    new.add((x, y))

                else:
                    new.add((2 * c - x, y))

            else:
                if y < c:
                    new.add((x, y))

                else:
                    new.add((x, 2 * c-y))

        s = new

    xs = [c[0] for c in s]
    ys = [c[1] for c in s]

    for i in range(max(ys) + 1):
        for j in range(max(xs) + 1):
            if (j, i) in s:
                print('#', end='')
            else:
                print(' ', end='')

        print()

    return ans

run_solutions(p1, p2)
