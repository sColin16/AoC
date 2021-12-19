import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *

from itertools import permutations, product, combinations
import numpy as np

def get_rotation_matrices():
    matrices = []

    for order in permutations([0, 1, 2]):

        signs = [[1, -1]] * 3

        for x, y, z in product(*signs):
            matrix = create_matrix(3, 3, 0)

            matrix[0][order[0]] = x
            matrix[1][order[1]] = y
            matrix[2][order[2]] = z

            if np.linalg.det(matrix) == 1:
                matrices.append(matrix)

    return matrices

def transform(distances, m):
    new = create_matrix(len(distances[0]), len(distances), [0, 0, 0])

    for i in range(len(distances)):
        for j in range(len(distances[0])):
            new[i][j] = list(np.matmul(m, distances[i][j]))

    return new

def count_matches(rowA, rowB):
    rowA = [tuple(element) for element in rowA]
    rowB = [tuple(element) for element in rowB]

    sA = set(rowA)
    sB = set(rowB)

    return len(sA.intersection(sB))

class Translation:
    def __init__(self, matrix, pos):
        self.matrix = matrix
        self.pos = pos

def extract_match(rowA, rowB):
    result = {}

    for i, a in enumerate(rowA):
        for j, b in enumerate(rowB):
            if a == b:
                return (i, j)

def diff(c1, c2):
    return [c1[i] - c2[i] for i in range(3)]

def add(c1, c2):
    return [c2[i] + c1[i] for i in range(3)]

def negate(c1):
    return [-c1[i] for i in range(3)]

def p1(raw, lines, sections, nums, *args, **kwargs):
    # Input parsing: store the measurements from each scanner in a multidimensional array
    beacons = []

    for section in sections:
        section = section[1:]

        row = []
        for line in section:
            row.append(stoil(line.split(',')))

        beacons.append(row)

    # Compute relative distances between all beacons: this is how we determine overlap
    # all_distances[i][j][k][l] represents the distances between beacons for scanner i under rotation j between beacons k and l
    all_distances = []

    # All 24 rotations are represnted by a 3x3 rotation matrix
    rm = get_rotation_matrices()

    for beacon in beacons:
        distances = create_matrix(len(beacon), len(beacon), [0, 0, 0])

        for i in range(len(beacon)):
            for j in range(len(beacon)):
                xdist = beacon[i][0] - beacon[j][0]
                ydist = beacon[i][1] - beacon[j][1]
                zdist = beacon[i][2] - beacon[j][2]

                distances[i][j] = [xdist, ydist,zdist]

        rotated_distances = [transform(distances, m) for m in rm]

        all_distances.append(rotated_distances)

    # When we find overlap, we record the way to convert between beacon coordiante systems
    # translations[i][j] stores the way to convert from beacon j to beacon i's coordinate system
    translations = create_matrix(len(beacons), len(beacons), None)

    # The number of matches required to consider the beacons sufficiently overlapped
    MATCH = 12

    # Iterate over every pair of scanners to identify overlaps between them
    for i in range(len(beacons)):
        first = all_distances[i][0]

        for j in range(i + 1, len(beacons)):
            second_all = all_distances[j]

            found = False

            # Iterate over all rotations of the second beacon's coordinate system
            for k, second in enumerate(second_all):
                m = rm[k]

                # Iterate over all rows in the two idstance matrices
                # Skip the final 11 (or MATCH-1) rows because 12 rows should match
                for fr in first[:-(MATCH-1)]:
                    for sr in second[:-(MATCH-1)]:
                        matches = count_matches(fr, sr)

                        if matches == 12:
                            # Determine the indices of two matching beacons
                            a_idx, b_idx = extract_match(fr, sr)

                            # Get coordinates of matching beacon relative to the first scanner
                            first_beacon_A = beacons[i][a_idx]

                            # Get coordinates of matching beacon, but transformed so that
                            # both coordinate systems are in the same rotational frame
                            first_beacon_B = np.matmul(m, beacons[j][b_idx])

                            # Determine the position of the second scanner relative to the first
                            posB = diff(first_beacon_A, first_beacon_B)

                            # Determine the rotation matrix to go from A -> B instead of B -> A
                            # This should just be the transpose since it's orthogonal
                            inv_m = np.linalg.inv(m)

                            # Determine the position of the first relative relative to the second
                            inv_pos = np.matmul(inv_m, negate(posB))

                            # Store the translations in the translation matrix
                            translationA = Translation(m, posB)
                            translationB = Translation(inv_m, inv_pos)

                            translations[i][j] = translationA
                            translations[j][i] = translationB

                            print(f'Found match between {i} and {j} for rotation {k}')

                            found = True
                            break

                    if found:
                        break

                if found:
                    break


    # We have a partial table of translations between scanners
    # We fill out the entire table so we have translations for all scanners relative to scanner 0
    changed = True
    while changed:          # It is necessary to run this a couple times to fill everything in
        changed = False

        # Iterate over every cell in the translation matrix
        for i in range(len(translations)):
            for j in range(len(translations)):

                # If we find an existing translation, we leverage it to create other translations
                if i != j and translations[i][j] is not None:

                    # Iterate over every column in row j to find translations we can leverage
                    for k in range(len(translations)):

                        # If we found a translation that will let us fill in a part of the table
                        # We compute the translation
                        if i != k and translations[j][k] is not None and translations[i][k] is None:
                            # Leverage linear algebgra to chain the rotation matrices
                            mat = np.matmul(translations[i][j].matrix, translations[j][k].matrix)

                            pos = add(np.matmul(translations[i][j].matrix, translations[j][k].pos), translations[i][j].pos)

                            translations[i][k] = Translation(mat, pos)
                            changed = True
                            print(f'Computed translation between {i} and {k}')

    # We throw all the final coordinates in a set to eliminate duplicates
    final = set()

    # Iterate over all the scanners to add their beacons relative to scanner 0
    for i, group in enumerate(beacons):
        # No translations needed for scanner 0
        if i == 0:
            for beacon in group:
                final.add(tuple(beacon))

        # Otherwise use the translation to place beacon locations relative to scanner 0 in set
        else:
            for beacon in group:
                trans = np.matmul(translations[0][i].matrix, beacon)
                trans = add(trans, translations[0][i].pos)

                final.add(tuple(trans))

    print(f'Total beacons: {len(final)}')

    # Also do part 2 since my solution is kinda slow
    # Just iterate over all the pairs of beacons to get the distances
    d = 0
    for i in range(1, len(beacons)):
        for j in range(i + 1, len(beacons)):
            dist_vec = diff(translations[0][i].pos, translations[0][j].pos)
            newd = int(sum([abs(elem) for elem in dist_vec]))

            d = max(d, newd)

    print(f'Maximum L-1 distance between beacons: {d}')

    return len(final), d

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0


    return ans

run_solutions(p1, p2)
