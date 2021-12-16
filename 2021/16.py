import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *

def evaluate_packets(bs):
    index = 0

    pv = int(bs[index: index+3], 2)
    pt = int(bs[index+3: index+6], 2)

    index += 6

    if pt == 4:
        value = ''

        while True:
            n = bs[index: index + 5]
            index += 5

            value += n[1:]

            if n[0] == '0':
                break

        return int(value, 2), index

    l = int(bs[index])
    index += 1

    if l == 0:
        total_bits = int(bs[index: index + 15], 2)
        index += 15
        start = index

        values = []

        value, end = evaluate_packets(bs[index:])
        values.append(value)
        index += end

        while index - start < total_bits:
            value, end = evaluate_packets(bs[index:])
            values.append(value)
            index += end

    else:
        total_packets = int(bs[index: index + 11], 2)
        index += 11
        values = []

        for i in range(total_packets):
            value, end = evaluate_packets(bs[index:])
            values.append(value)
            index += end

    if pt == 0:
        return sum(values), index

    if pt == 1:
        return math.prod(values), index

    if pt == 2:
        return min(values), index

    if pt == 3:
        return max(values), index

    if pt == 5:
        return ((1 if values[0] > values[1] else 0), index)

    if pt == 6:
        return ((1 if values[0] < values[1] else 0), index)

    if pt == 7:
        return ((1 if values[0] == values[1] else 0), index)

def sum_versions(bs):
    index = 0

    pv = int(bs[index: index+3], 2)
    pt = int(bs[index+3: index+6], 2)

    index += 6

    if pt == 4:
        while True:
            n = bs[index: index + 5]
            index += 5

            if n[0] == '0':
                break

        return pv, index

    l = int(bs[index])
    index += 1

    if l == 0:
        total_bits = int(bs[index: index + 15], 2)
        index += 15
        start = index

        values = [pv]

        value, end = sum_versions(bs[index:])
        values.append(value)
        index += end

        while index - start < total_bits:
            value, end = sum_versions(bs[index:])
            values.append(value)
            index += end

    else:
        total_packets = int(bs[index: index + 11], 2)
        index += 11
        values = [pv]

        for i in range(total_packets):
            value, end = sum_versions(bs[index:])
            values.append(value)
            index += end


    return sum(values), index

def p1(raw, lines, sections, nums, *args, **kwargs):
    info = lines[0]
    num = int(info, 16)

    bs = "{0:b}".format(num)

    # Pad the hexadecimal number with appropriate number of 0 bits
    while len(bs) % 8 != 0:
        bs = '0' + bs

    ans, _ = sum_versions(bs)

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    info = lines[0]
    num = int(info, 16)

    bs = "{0:b}".format(num)

    # Pad the hexadecimal number with appropriate number of 0 bits
    while len(bs) % 8 != 0:
        bs = '0' + bs

    ans, _ = evaluate_packets(bs)

    return ans

run_solutions(p1, p2)
