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

    d = {}
    for line in sections[1]:
        a, b = line.split(' -> ')

        d[a] = b

    s = lines[0]

    pairs = defaultdict(int)
    for j in range(len(s) - 1):
        pairs[s[j:j+2]] += 1

    for i in range(10):
        newp = defaultdict(int)
        ins = [''] * (len(s) - 1)

        for j in range(len(s) - 1):
            if s[j:j+2] in d:
                ins[j] = d[s[j:j+2]]

        new = ''

        for j in range(len(s) - 1):
            new += s[j]
            new += ins[j]

        new += s[-1]

        s = new

    f = count_freq(list(s))

    large = max([(value, key) for key, value in f.items()])
    small = min([(value, key) for key, value in f.items()])

    ans = large[0] - small[0]

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

    large = max([(value, key) for key, value in counts.items()])
    small = min([(value, key) for key, value in counts.items()])

    # We double-counted all the letters, so divide by 2
    ans = int((large[0] - small[0]) / 2)

    return ans

run_solutions(p1, p2)
