import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    alg = [1 if s == '#' else 0 for s in sections[0][0]]

    img = defaultdict(lambda: 0)

    for i, row in enumerate(sections[1]):
        for j, num in enumerate(row):
            if num == '#':
                img[(i, j)] = 1

    default = 0
    for i in range(50):
        new_img = {}
        xs = [key[0] for key, v in img.items()]
        ys = [key[1] for key, v in img.items()]

        for j in range(min(xs) - 1, max(xs) + 2):
            for k in range(min(ys) - 1, max(ys) + 2):
                val = 0

                for a in range(-1, 2):
                    for b in range(-1, 2):
                        p = img[(j + a, k + b)]

                        val += p

                        val *= 2

                val /= 2
                val = int(val)

                if alg[val] != default:
                    new_img[(j, k)] = int(not default)

        prev_d = default

        if default == 0:
            default = alg[0]

        elif default == 1:
            default = alg[511]

        if prev_d == default:
            img = defaultdict(lambda: default, new_img)

        else:
            new_new_img = defaultdict(lambda: default)

            xs = [key[0] for key, v in new_img.items()]
            ys = [key[1] for key, v in new_img.items()]

            for i in range(min(xs), max(xs) + 1):
                for j in range(min(ys), max(ys) + 1):
                    if (i, j) not in new_img:
                        new_new_img[(i, j)] = prev_d

            img = new_new_img

        print(len(img))

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    return ans

run_solutions(p1, p2)
