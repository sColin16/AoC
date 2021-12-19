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

        signs = [[1, -1], [1, -1], [1, -1]]

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

def extract_matches(rowA, rowB):
    result = {}

    for i, a in enumerate(rowA):
        for j, b in enumerate(rowB):
            if a == b:
                result[i] = j

    return result

def diff(c1, c2):
    return [c1[i] - c2[i] for i in range(3)]

def add(c1, c2):
    return [c2[i] + c1[i] for i in range(3)]

def negate(c1):
    return [-c1[i] for i in range(3)]

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    beacons = []
    for section in sections:
        section = section[1:]

        row = []
        for line in section:
            row.append(list(map(int, line.split(','))))

        beacons.append(row)

    all_distances = []

    for beacon in beacons:
        distances = create_matrix(len(beacon), len(beacon), [0, 0, 0])

        for i in range(len(beacon)):
            for j in range(len(beacon)):
                xdist = beacon[i][0] - beacon[j][0]
                ydist = beacon[i][1] - beacon[j][1]
                zdist = beacon[i][2] - beacon[j][2]

                distances[i][j] = [xdist, ydist,zdist]

        #print(*distances, sep='\n')
        #print()

        all_distances.append(distances)

    rm = get_rotation_matrices()
    translations = create_matrix(len(beacons), len(beacons), None)

    MATCH = 12
    for i in range(len(beacons)):
        first = all_distances[i]

        for j in range(i + 1, len(beacons)):
            second = all_distances[j]

            mmatch = 0
            found = False
            for k, m in enumerate(rm):
                t = transform(second, m)

                for fr in first:
                    for sr in t:
                        matches = count_matches(fr, sr)

                        if matches == 12:
                            #print('Bingo', i, j, k)
                            cv = extract_matches(fr, sr)
                            f = list(cv.items())[0]
                            first_beacon_A = beacons[i][f[0]]
                            first_beacon_B = np.matmul(m, beacons[j][f[1]])

                            posB = diff(first_beacon_A, first_beacon_B)

                            translation = Translation(m, posB)
                            translations[i][j] = translation

                            translationB = Translation(np.linalg.inv(m), np.matmul(np.linalg.inv(m), negate(posB)))
                            translations[j][i] = translationB

                            print(i, j, k, posB)
                            print(j, i, np.linalg.inv(m), np.matmul(np.linalg.inv(m), negate(posB)))

                            found = True
                            break

                    if found:
                        break

                if found:
                    break

    # Find all the mappings from a beacon to beacon 0
    changed = True
    while changed:
        changed = False
        for i in range(len(translations)):
            for j in range(len(translations)):
                if i != j and translations[i][j] is not None:
                    for k in range(len(translations)):
                        if i != k and translations[j][k] is not None and translations[i][k] is None:
                            pos = add(np.matmul(translations[i][j].matrix, translations[j][k].pos), translations[i][j].pos)
                            mat = np.matmul(translations[i][j].matrix, translations[j][k].matrix)

                            translations[i][k] = Translation(mat, pos)
                            changed = True
                            print('tran', i, k, pos)

    final = set()

    for beacon in beacons[0]:
        final.add(tuple(beacon))

    for i, group in enumerate(beacons):
        if i == 0:
            for beacon in group:
                final.add(tuple(beacon))

        else:
            for beacon in group:
                trans = np.matmul(translations[0][i].matrix, beacon)
                trans = add(trans, translations[0][i].pos)

                final.add(tuple(trans))

    print(len(final))

    d = 0
    for i in range(1, len(beacons)):
        for j in range(i + 1, len(beacons)):
            newd = abs(translations[0][i].pos[0] - translations[0][j].pos[0]) + abs(translations[0][i].pos[1] - translations[0][j].pos[1]) + abs(translations[0][i].pos[2] - translations[0][j].pos[2])

            d = max(d, newd)

    print(d)

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0


    return ans

run_solutions(p1, p2)
