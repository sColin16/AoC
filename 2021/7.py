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
    
    # The mean is close to this b/c the total cost is n(n+1)/2
    # It's not exact because of the n+1. I can't figure out the closed-form
    # solution, but it seems to be within one of the mean...
    # Still an O(n) solution... but maybe wrong on some inputs
    m = round(mean(p))

    a1 = 0
    for i in p:
        n = abs(i - m)

        a1 += n* (n+1)/2

    a2 = 0
    for i in p:
        n = abs(i - m - 1)

        a2 += n * (n + 1) / 2

    a3 = 0
    for i in p:
        n = abs(i - m + 1)

        a3 += n * (n + 1) / 2

    ans = min(a1, a2, a3)

    return int(ans)

run_solutions(p1, p2)
