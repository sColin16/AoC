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

    d = dmatrix(lines)
    g = Grid(d)
    for i in range(100):
        for j in range(10):
            for k in range(10):
                g.content[j][k] += 1

        flash = create_matrix(10, 10, False)
        changed = True

        while changed:
            changed = False

            for j in range(10):
                for k in range(10):
                    if g.get(j, k) > 9 and flash[j][k] == False:
                        flash[j][k] = True
                        ans += 1
                        changed = True

                        for a, b in g.get_adj8(j, k):
                            g.content[a][b] += 1

        for j in range(10):
            for k in range(10):
                if flash[j][k]:
                    g.content[j][k] = 0

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = dmatrix(lines)
    g = Grid(d)
    i = 1
    while True:
        for j in range(10):
            for k in range(10):
                g.content[j][k] += 1

        flash = create_matrix(10, 10, False)
        changed = True

        while changed:
            changed = False

            for j in range(10):
                for k in range(10):
                    if g.get(j, k) > 9 and flash[j][k] == False:
                        flash[j][k] = True
                        changed = True

                        for a, b in g.get_adj8(j, k):
                            g.content[a][b] += 1

        if all([all(f) for f in flash]):
            return i

        for j in range(10):
            for k in range(10):
                if flash[j][k]:
                    g.content[j][k] = 0

        i += 1

run_solutions(p1, p2)
