import re
import sys
import argparse
import math

from collections import defaultdict

import sys
sys.path.append('../')

from executor import *
from helpers import *

from heapq import *
from math import inf

def p1(raw, lines, sections, nums, *args, **kwargs):
    g = Grid(dmatrix(lines))
    distances = defaultdict(lambda: inf)

    done = set()
    distances[(0, 0)] = 0
    heap = [(0, (0, 0))]

    while len(heap) > 0:
        distance, coord = heappop(heap)

        # Skip if this node was processed at a shorter distance
        if coord in done:
            continue

        # If we are processing the target coordinate, we have found the solution
        if coord == (g.width - 1, g.height - 1):
            return distance

        for test_coord in g.get_adj4(*coord):
            if test_coord not in done and distance + g.get(*test_coord) < distances[test_coord]:
                # Relaxation step
                new_dist = distance + g.get(*test_coord)
                distances[test_coord] = new_dist

                # Add the point to the priority queue
                heappush(heap, (new_dist, test_coord))

        # Mark the node as processed
        done.add(coord)

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    original_tile = dmatrix(lines)
    width = len(lines[0])
    height = len(lines)
    all_tiles = create_matrix(5 * width, 5 * height, 0)

    for i in range(height):
        for j in range(width):
            for k in range(5):
                for l in range(5):
                    all_tiles[i + k * height][j + l * width] =\
                        (original_tile[i][j] + k + l - 1) % 9 + 1


    g = Grid(all_tiles)
    distances = defaultdict(lambda: inf)

    done = set()
    distances[(0, 0)] = 0
    heap = [(0, (0, 0))]

    while len(heap) > 0:
        distance, coord = heappop(heap)

        # Skip if this node was processed at a shorter distance
        if coord in done:
            continue

        # If we are processing the target coordinate, we have found the solution
        if coord == (g.height - 1, g.width - 1):
            return distance

        for test_coord in g.get_adj4(*coord):
            if test_coord not in done and distance + g.get(*test_coord) < distances[test_coord]:
                # Relaxation step
                new_dist = distance + g.get(*test_coord)
                distances[test_coord] = new_dist

                # Add the point to the priority queue
                heappush(heap, (new_dist, test_coord))

        # Mark the node as processed
        done.add(coord)

run_solutions(p1, p2)
