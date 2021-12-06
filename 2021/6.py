import re
import sys
import argparse
import math

import sys
sys.path.append('../')

from executor import *
from helpers import *

from collections import defaultdict

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    ages = stoil(lines[0].split(','))

    DAYS = 80
    for i in range(DAYS):
        new_ages = []

        for age in ages:
            if age > 0:
                new_ages.append(age - 1)

            else:
                new_ages.append(6)
                new_ages.append(8)

        ages = new_ages

    ans = len(ages)

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    DAYS = 256
    ages = stoil(lines[0].split(','))

    aged = count_freq(ages)

    for i in range(DAYS):
        new_aged = defaultdict(int)

        for key, value in aged.items():
            if key > 0:
                new_aged[key - 1] += value

            else:
                new_aged[6] += value
                new_aged[8] += value

        aged = new_aged

    for key, value in aged.items():
        ans += value

    return ans

run_solutions(p1, p2)
