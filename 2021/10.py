import re
import sys
import argparse
import math

from collections import defaultdict

import sys
sys.path.append('../')

from executor import *
from helpers import *

from statistics import median

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    m = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    for i, line in enumerate(lines):
        s = []
        for c in list(line):
            if c in '({[<':
                s.append(c)

            else:
                n = s.pop()

                if c != m[n]:
                    ans += scores[c]
                    break

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    m = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    invalid = [False] * len(lines)

    for i, line in enumerate(lines):
        s = []
        for c in list(line):
            if c in '({[<':
                s.append(c)

            else:
                n = s.pop()

                if c != m[n]:
                    invalid[i]= True
                    break

    newl = [lines[i] for i in range(len(lines)) if not invalid[i]]
    a = [0] * len(newl)

    for i, line in enumerate(newl):
        s = []
        for c in list(line):
            if c in '({[<':
                s.append(c)

            else:
                s.pop()

        for c in reversed(s):
            a[i] *= 5

            a[i] += scores[m[c]]

    ans = median(a)

    return ans

run_solutions(p1, p2)
