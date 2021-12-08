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

    for line in lines:
        after = line.split('|')[1]

        for chars in after.split(' '):
            if len(chars) in [2, 3, 4, 7]:
                ans += 1

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    for line in lines:
        before, after = line.split('|')

        l = [''] * 10
        # Identify the letters that we know
        for a in before.split():
            if len(a) == 2:
                l[1] = a

            if len(a) == 3:
                l[7] = a

            if len(a) == 4:
                l[4] = a

            if len(a) == 7:
                l[8] = a

        # Then go through some logic I can no longer explain
        for a in before.split():
            if len(a) == 5 and l[1][0] in a and l[1][1] in a:
                l[3] = a

        fourl = ''
        for char in l[4]:
            if char not in l[1]:
                fourl += char

        for a in before.split():
            if len(a) == 5 and fourl[0] in a and fourl[1] in a:
                l[5] = a

        for a in before.split():
            if len(a) == 5 and a != l[3] and a != l[5]:
                l[2] = a

        for a in before.split():
            if len(a) == 6 and (l[1][0] not in a or l[1][1] not in a):
                l[6] = a

        for a in before.split():
            if len(a) == 6 and fourl[0] in a and fourl[1] in a and a != l[6]:
                l[9] = a

        for a in before.split():
            if len(a) == 6 and a!= l[9] and a != l[6]:
                l[0] = a

        def matches(test, defi):
            if len(test) != len(defi):
                return False

            for letter in defi:
                if letter not in test:
                    return False

            return True

        result = 0
        for chars in after.split():
            for i in range(10):
                if matches(chars, l[i]):
                    result = result * 10 + i

                    break

        ans += result

    return ans

run_solutions(p1, p2)
