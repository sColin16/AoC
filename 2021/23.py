import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *

def flood(state, r, c, l, depth):
    valid = set([(1, i + 1) for i in range(11)])

    for i in range(2, depth + 2):
        valid.add((i, 3))
        valid.add((i, 5))
        valid.add((i, 7))
        valid.add((i, 9))

    def get_neighbors(loc):
        a, b = loc

        possible = [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]
        valid_cells = [p for p in possible if p in valid]

        return [p for p in valid_cells if state.get(p) is None]

    return flood_fill((r, c), get_neighbors)

def hash_d(d):
    return tuple(sorted([(key, val) for key, val in d.items()]))

def vis(state, depth):
    for i in range(11):
        print('.' if state.get((1, i + 1)) is None else state.get((1, i + 1)), end='')

    print()

    for i in range(2, depth + 2):
        print('  ', end='')
        for j in range(3, 11, 2):
            print('.' if state.get((i, j)) is None else state.get((i, j)), end='')
            print(' ', end='')

        print()

# Determine is a letter at a given location is considered solved
def solved(letter, loc, state, depth):
    correct = {
        'A': 3,
        'B': 5,
        'C': 7,
        'D': 9
    }

    if loc[1] != correct[letter]:
        return False

    for i in range(loc[0] + 1, depth + 2):
        if state.get((i, loc[1])) != letter:
            return False

    return True

def move_piece(state, loc, new_loc):
    new_state = state.copy()
    letter = new_state[loc]

    del new_state[loc]

    new_state[new_loc] = letter

    return new_state

COSTS = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
}

def get_neighbors(state, depth): 
    neighbors = []

    for loc, letter in state.items():
        # Don't move any pieces already solved
        if solved(letter, loc, state, depth):
            continue

        new_positions = flood(state, loc[0], loc[1], letter, depth)

        for move, cost in new_positions.items():
            # If in a room, can only move into hallway non-entrances
            if loc[0] >= 2 and move[0] == 1 and move[1] not in (3, 5, 7, 9):
                new_state = move_piece(state, loc, move)

                neighbors.append((new_state, cost * COSTS[letter]))

            # If in a hallway and moving solves the location it is valid
            elif solved(letter, move, state, depth):
                new_state = move_piece(state, loc, move)

                neighbors.append((new_state, cost * COSTS[letter]))

    return neighbors

def p1(raw, lines, sections, nums, *args, **kwargs):
    start = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in 'ABCD':
                start[(i, j)] = char

    target = {
            (2, 3): 'A',
            (3, 3): 'A',
            (2, 5): 'B',
            (3, 5): 'B',
            (2, 7): 'C',
            (3, 7): 'C',
            (2, 9): 'D',
            (3, 9): 'D'
    }

    return dijsktras(start, target, lambda node: get_neighbors(node, 2), hash_d)

def p2(raw, lines, sections, nums, *args, **kwargs):
    start = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in 'ABCD':
                if i != 3:
                    start[(i, j)] = char
                else:
                    start[(i + 2, j)] = char

    start[(3, 3)] = 'D'
    start[(4, 3)] = 'D'
    start[(3, 5)] = 'C'
    start[(4, 5)] = 'B'
    start[(3, 7)] = 'B'
    start[(4, 7)] = 'A'
    start[(3, 9)] = 'A'
    start[(4, 9)] = 'C'

    target = {
            (2, 3): 'A',
            (3, 3): 'A',
            (4, 3): 'A',
            (5, 3): 'A',
            (2, 5): 'B',
            (3, 5): 'B',
            (4, 5): 'B',
            (5, 5): 'B',
            (2, 7): 'C',
            (3, 7): 'C',
            (4, 7): 'C',
            (5, 7): 'C',
            (2, 9): 'D',
            (3, 9): 'D',
            (4, 9): 'D',
            (5, 9): 'D'
    }

    return dijsktras(start, target, lambda node: get_neighbors(node, 4), hash_d)

run_solutions(p1, p2)
