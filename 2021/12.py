import re
import sys
import argparse
import math

from collections import defaultdict

import sys
sys.path.append('../')

from executor import *
from helpers import *

# My solution to this problem is really bad
# Also, part 2 is comically slow probably because of that function to check if
# cave was visited twice, but also because this solution is bad
def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = defaultdict(list)

    for line in lines:
        a, b = line.split('-')
        d[a].append(b)
        d[b].append(a)

    
    q = [['start']]
    found = []

    while len(q) > 0:
        n = q.pop(0)

        for neighbor in d[n[-1]]:
            if neighbor == 'end':
                c = n[:]
                c.append(neighbor)
                found.append(c)
                continue

            if neighbor.isupper() or n.count(neighbor) == 0:
                copy = n[:]
                copy.append(neighbor)
                q.append(copy)

    ans = len(found)
    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    d = defaultdict(list)

    for line in lines:
        a, b = line.split('-')
        d[a].append(b)
        d[b].append(a)
    
    q = [['start']]
    found = []

    def count_lower(l):
        f = count_freq(l)

        for key, value in f.items():
            if key != 'start' and key.islower() and value >= 2:
                return True

        return False

    while len(q) > 0:
        n = q.pop(0)

        for neighbor in d[n[-1]]:
            if neighbor == 'end':
                c = n[:]
                c.append(neighbor)
                found.append(c)
                continue

            if not neighbor == 'start' and (neighbor.isupper() or (count_lower(n) and n.count(neighbor) == 0) or (not count_lower(n) and n.count(neighbor) < 2)):
                copy = n[:]
                copy.append(neighbor)
                q.append(copy)

    ans = len(found)

    return ans

run_solutions(p1, p2)
