import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *

from itertools import product

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    cubes = set()

    for line in lines:
        s, info = line.split(' ')

        xs, ys, zs = info.split(',')

        xa = stoil(xs[2:].split('..'))
        ya = stoil(ys[2:].split('..'))
        za = stoil(zs[2:].split('..'))

        if xa[0] <= -50 or xa[1] >= 50:
            continue

        for i in range(xa[0], xa[1] + 1):
            for j in range(ya[0], ya[1] + 1):
                for k in range(za[0], za[1] + 1):
                    if s == 'on':
                        cubes.add((i, j, k))
                    elif (i, j, k) in cubes:
                        cubes.remove((i, j, k))

    ans = len(cubes)

    return ans

def overlap1D(x1, x2, y1, y2):
    # Contianed A
    if x1 >= y1 and x1 <+ y2 and x2 >+ y1 and x2 <= y2:
        return (x1, x2)

    # Contained B
    if y1 >= x1 and y1 <= x2 and y2 >= x1 and y2 <= x2:
        return (y1, y2)

    # Shifted A
    if x1 <= y1 and x1 <= y2 and x2 >= y1 and x2 <= y2:
        return (y1, x2)

    # Shifted B
    if y1 <= x1 and y1 <= x2 and y2 >= x1 and y2 <= x2:
        return (x1, y2)

    return None

def overlap(r1, r2):
    xo = overlap1D(r1[0], r1[1], r2[0], r2[1])
    yo = overlap1D(r1[2], r1[3], r2[2], r2[3])
    zo = overlap1D(r1[4], r1[5], r2[4], r2[5])

    if xo is not None and yo is not None and zo is not None:
        return (*xo, *yo, *zo)

    return None

def size(r):
    x = r[1] - r[0] + 1
    y = r[3] - r[2] + 1
    z = r[5] - r[4] + 1

    if x <=0 or y <= 0 or z <= 0:
        return 0

    return x * y * z

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    regions = set()

    for line in lines:
        s, info = line.split(' ')

        xs, ys, zs = info.split(',')

        xa = stoil(xs[2:].split('..'))
        ya = stoil(ys[2:].split('..'))
        za = stoil(zs[2:].split('..'))

        t = (xa[0], xa[1], ya[0], ya[1], za[0], za[1])

        overlapping = []
        for region in regions:
            o = overlap(t, region)

            if o is not None:
                overlapping.append((region, o))

        if len(overlapping) > 0:
            for region, o in overlapping:
                regions.remove(region)

            for region, o in overlapping:
                xs = [(region[0], o[0] - 1), (o[0], o[1]), (o[1] + 1, region[1])]
                ys = [(region[2], o[2] - 1), (o[2], o[3]), (o[3] + 1, region[3])]
                zs = [(region[4], o[4] - 1), (o[4], o[5]), (o[5] + 1, region[5])]

                for cube in product(xs, ys, zs):
                    cube = (*cube[0], *cube[1], *cube[2])

                    if size(cube) > 0 and cube != o:
                        regions.add(cube)

        if s == 'on':
            regions.add(t)
            pass

    for region in regions:
        ans += size(region)

    return ans

run_solutions(p1, p2)
