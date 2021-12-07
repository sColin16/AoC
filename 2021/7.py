import re
import sys
import argparse
import math

from collections import defaultdict

import sys
sys.path.append('../')

from statistics import median, mean

from executor import *
from helpers import *

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    p = stoil(lines[0].split(','))  

    # The median is guaranteed to be the answer on this part!
    # It's an O(n) solution
    m = median(p)

    for i in p:
        ans += abs(i - m)

    return int(ans)

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    p = stoil(lines[0].split(','))
    
    m = mean(p)

    # xbar plus or minus 0.5 is a bound for the optimal real midpoint
    # I look at all nearby integers to find the optimal integer midpoint
    # It's possible that a tighter bound exists (e.g floor(xbar) to ceil(xbar))
    m1 = math.floor(m - 0.5)
    m2 = math.ceil(m + 0.5)

    costs = []
    for mid in range(m1, m2 + 1):
        cost = 0
        for i in p:
            n = abs(i - mid)

            cost += n * (n + 1) / 2

        costs.append(cost)

    ans = int(min(costs))

    return ans

run_solutions(p1, p2)
