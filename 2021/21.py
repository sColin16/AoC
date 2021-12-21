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
    rolls = 0

    scores = [0, 0]
    a = int(lines[0].split(' ')[-1]) - 1
    b = int(lines[1].split(' ')[-1]) - 1

    n = 1
    turn = 1

    while max(scores) < 1000:
        roll = 0
        for i in range(3):
            roll += n

            if n == 100:
                n = 1
            else:
                n += 1

        if turn == 1:
            a = (a + roll) % 10

            scores[0] += a + 1

            turn = 2

        else:
            b = (b + roll) % 10

            scores[1] += b + 1

            turn = 1

        rolls += 3

    if scores[0] >= 1000:
        ans = rolls * scores[1]

    if scores[1] >= 1000:
        ans = rolls * scores[0]

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    a = int(lines[0].split(' ')[-1]) - 1
    b = int(lines[1].split(' ')[-1]) - 1

    scores = {(0, 0, a, b, 1): 1}

    wins = [0, 0]
    while len(scores) > 0:
        new_scores = defaultdict(int)
        for info, count in scores.items():
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        s1, s2, l1, l2, turn = info

                        roll = i + j + k + 3

                        if turn == 1:
                            l1 = (l1 + roll) % 10
                            s1 += l1 + 1

                        else:
                            l2 = (l2 + roll) % 10
                            s2 += l2 + 1

                        if s1 >= 21:
                            wins[0] += count

                        elif s2 >= 21:
                            wins[1] += count

                        else:
                            new_scores[(s1, s2, l1, l2, 1 if turn == 2 else 2)] += count

        scores = new_scores

    ans = max(wins)

    return ans

run_solutions(p1, p2)
