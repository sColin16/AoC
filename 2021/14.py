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

    d = {}
    for line in sections[1]:
        a, b = line.split(' -> ')

        d[a] = b

    s = lines[0]

    for i in range(10):
        news = ''
        for j in range(len(s) - 1):
            news += s[j]

            if s[j:j+2] in d:
                news += d[s[j:j+2]]

        s = news + s[-1]

    counts = Counter(s)
    sort = counts.most_common()

    ans = sort[0][1] - sort[-1][1]

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = {}
    for line in sections[1]:
        a, b = line.split(' -> ')

        d[a] = b

    s = lines[0]

    pairs = defaultdict(int)
    for j in range(len(s) - 1):
        pairs[s[j:j+2]] += 1

    for i in range(40):
        newp = defaultdict(int)

        for key, value in pairs.items():
            if key in d:
                newp[key[0] + d[key]] += value
                newp[d[key] + key[1]] += value

        pairs = newp

    counts = defaultdict(int)

    for key, value in pairs.items():
        counts[key[0]] += value
        counts[key[1]] += value

    # Add the first and last character since those aren't double-counted
    counts[lines[0][0]] += 1
    counts[lines[0][-1]] += 1

    counts = Counter(counts)
    sort = counts.most_common()

    ans = int((sort[0][1] - sort[-1][1])/2)

    return ans

run_solutions(p1, p2)
