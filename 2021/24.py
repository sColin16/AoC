import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *

def ex(inp, prog):
    '''
    Brute force executor of arbitrary programs
    '''

    inp_idx = 0
    reg = defaultdict(int)

    for line in prog:
        part = line.split(' ')

        if len(part) > 2:
            second = reg[part[2]] if part[2] in 'wxyz' else int(part[2])

        if part[0] == 'inp':
            reg[part[1]] = int(inp[inp_idx])
            inp_idx += 1

        elif part[0] == 'add':
            reg[part[1]] = reg[part[1]] + second

        elif part[0] == 'mul':
            reg[part[1]] = reg[part[1]] * second

        elif part[0] == 'div':
            if second == 0:
                #print('Divide by 0')
                return None

            reg[part[1]] = reg[part[1]] // second

        elif part[0] == 'mod':
            if reg[part[1]] < 0 or second <= 0:
                #print('Mod error')
                return None

            reg[part[1]] = reg[part[1]] % second

        elif part[0] == 'eql':
            reg[part[1]] = 1 if reg[part[1]] == second else 0

    return reg['z']

def alg(w, z, a, b, c):
    '''
    Simplified version of a section of the algorithm in the actual input

    w is the input between 1 and 9
    z is the output from the previous section
    a, b, and c are the constants that are different in each section
    '''

    x = (z % 26) + b

    x = 1 if x != w else 0

    y = 25 * x + 1

    z = (z // a) * y

    y = x * (w + c)

    return z + y

def solve_t1(inp, target):
    '''
    Solves "Type 1" sections, when a = 1 and b < 0

    Determines the input w and zs that will obtain the target z

    There are possibly very many of these
    '''

    a, b, c = inp

    sols = []

    # Find the main sequences solutions
    for w in range(1, 10):
        if target % 26 == c + w:
            for i in range(26):
                if (i + 26 * (target // 26)) % 26 != -b + w:
                    sols.append((w, i + 26 * (target // 26)))

    # Find the "hole" solutions
    for w in range(1, 10):
        sols.append((w, -b + w + 26 * target))

    return sols

def solve_t2(inp, target):
    '''
    Solves "Type 2" sections, when a = 26 and b > 0

    Determines the input z and w needed to get the target

    Guaranteed to only be one such solution, if it exists at all
    '''

    a, b, c = inp

    for w in range(1, 10):
        if target % 26 == c + w:
            return [(w, target // 26)]

    return []

def solve(inp, target):
    if inp[0] == 1:
        return solve_t2(inp, target)

    else:
        return solve_t1(inp, target)

def get_inputs(lines):
    inputs = []

    for i in range(14):
        new = []
        for j in range(18):
            if j == 4:
                new.append(int(lines[i * 18 + j].split(' ')[2]))

            elif j == 5:
                new.append(int(lines[i * 18 + j].split(' ')[2]))

            elif j == 15:
                new.append(int(lines[i * 18 + j].split(' ')[2]))

        inputs.append(new)

    return inputs

def p1(raw, lines, sections, nums, *args, **kwargs):
    inputs = get_inputs(lines)

    # Stores target, solution pairs which we can use to avoid duplicates
    q = {
        0: tuple([0] * 14)
    }

    for i in reversed(range(14)):
        new_q = {}

        for target_z, p_sol in q.items():
            sols = solve(inputs[i], target_z)

            for w, z in sols:
                new_sol = list(p_sol)
                new_sol[i] = w
                new_sol = tuple(new_sol)

                if new_q.get(z) is None or new_q.get(z) < new_sol:
                    new_q[z] = new_sol

        q = new_q

    ans = ''.join(str(a) for a in q[0])

    return ans

def count_models(inputs):
    # Stores the number of candidate solutions associated with each target z value
    q = {
        0: 1
    }

    for i in reversed(range(14)):
        new_q = defaultdict(int)

        for target_z, p_sol in q.items():
            sols = solve(inputs[i], target_z)

            for w, z in sols:
                new_q[z] += p_sol

        q = new_q

    return q[0]

def p2(raw, lines, sections, nums, *args, **kwargs):
    inputs = get_inputs(lines)

    # Stores target, solution pairs which we can use to avoid duplicates
    q = {
        0: tuple([0] * 14)
    }

    for i in reversed(range(14)):
        new_q = {}

        for target_z, p_sol in q.items():
            sols = solve(inputs[i], target_z)

            for w, z in sols:
                new_sol = list(p_sol)
                new_sol[i] = w
                new_sol = tuple(new_sol)

                if new_q.get(z) is None or new_q.get(z) > new_sol:
                    new_q[z] = new_sol

        q = new_q

    ans = ''.join(str(a) for a in q[0])

    print(f'BONUS: Number of model numbers accepted {count_models(inputs)}')

    return ans

run_solutions(p1, p2)
