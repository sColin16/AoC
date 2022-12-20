import re
import sys
import argparse
import math

from collections import defaultdict, Counter
from dataclasses import dataclass

import sys
sys.path.append('../')

from executor import *
from helpers import *

m = {}
def solve(inp):
    if inp in m:
        return m[inp]

    blueprint, ore_robots, clay_robots, ob_robots, geo_robots, ore, clay, obsidian, time = inp
    a, b, (c, d), (e, f) = blueprint

    if time == 0:
        return 0

    new_ore = ore + ore_robots
    new_clay = clay + clay_robots
    new_ob = obsidian + ob_robots

    sol = 0
    geo_build = (ore >= e and obsidian >= f)
    ob_build = (ore >= c and clay >= d)

    if geo_build:
        pos_sol = solve((blueprint, ore_robots, clay_robots, ob_robots, geo_robots + 1, new_ore - e, new_clay, new_ob - f, time - 1))
        sol = max(sol, pos_sol)

    if not geo_build and ob_build:
        pos_sol = solve((blueprint, ore_robots, clay_robots, ob_robots + 1, geo_robots, new_ore - c, new_clay - d, new_ob, time - 1))
        sol = max(sol, pos_sol)

    if not geo_build and ore >= b:
        pos_sol = solve((blueprint, ore_robots, clay_robots + 1, ob_robots, geo_robots, new_ore - b, new_clay, new_ob, time - 1))
        sol = max(sol, pos_sol)

    if not geo_build and ore >= a:
        pos_sol = solve((blueprint, ore_robots + 1, clay_robots, ob_robots, geo_robots, new_ore - a, new_clay, new_ob, time - 1))
        sol = max(sol, pos_sol)

    if not geo_build and (ore < a or ore < b or not ob_build or not geo_build):
        pos_sol = solve((blueprint, ore_robots, clay_robots, ob_robots, geo_robots, new_ore, new_clay, new_ob, time - 1))
        sol = max(sol, pos_sol)

    m[inp] = sol + geo_robots

    if len(m) % 100000 == 0:
        print(len(m))
    return m[inp]

def p1(raw, lines, sections, nums, *args, **kwargs):
    global m
    m = {}
    ans = 0

    blueprints = []
    for line in lines:
        _, a = line.split(': ')
        b = a.split('. ')

        c = b[0].split('costs ')
        c = int(c[1].split(' ')[0])

        d = b[1].split('costs ')
        d = int(d[1].split(' ')[0])

        e = b[2].split('costs ')[1]
        e = e.split(' ')
        e, f = int(e[0]), int(e[3])

        g = b[3].split('costs ')[1]
        g = g.split(' ')
        g, h = int(g[0]), int(g[3])

        blueprints.append((c, d, (e, f), (g, h)))

    for i, bl in enumerate(blueprints):
        print("PROCESSING", i)
        m = {}
        ans += (i + 1) * solve((bl, 1, 0, 0, 0, 0, 0, 0, 24))

    return ans

m2 = {}
def solve2(inp):
    if inp in m2:
        return m2[inp]

    blueprint, ore_robs, clay_robs, ob_robs, geo_robs, ore, clay, ob, time = inp
    a, b, (c, d), (e, f) = blueprint

    if time == 0:
        return 0

    new_ore = ore + ore_robs
    new_clay = clay + clay_robs
    new_ob = ob + ob_robs

    geo_build = (ore >= e and ob >= f)
    ob_build = (ore >= c and clay >= d and ob_robs < f)
    clay_build = (ore >= b and clay_robs < d)
    ore_build = (ore >= a and ore_robs < max(a, b, c, e))

    ore_cap = (max(a, b, c, e) - ore_robs) * (time - 1) + ore_robs
    clay_cap = (d - clay_robs) * (time - 1) + clay_robs
    ob_cap = (f - ob_robs) * (time - 1) + ob_robs
    sol = 0
    if geo_build:
        pos_sol = solve2((blueprint, ore_robs, clay_robs, ob_robs, geo_robs + 1, min(new_ore - e, ore_cap), min(new_clay, clay_cap), min(new_ob - f, ob_cap), time - 1))
        sol = max(sol, pos_sol)

    if ob_build:
        pos_sol = solve2((blueprint, ore_robs, clay_robs, ob_robs + 1, geo_robs, min(new_ore - c, ore_cap), min(new_clay - d, clay_cap), min(new_ob, ob_cap), time - 1))
        sol = max(sol, pos_sol)

    if clay_build:
        pos_sol = solve2((blueprint, ore_robs, clay_robs + 1, ob_robs, geo_robs, min(new_ore - b, ore_cap), min(new_clay, clay_cap), min(new_ob, ob_cap), time - 1))
        sol = max(sol, pos_sol)

    if ore_build:
        pos_sol = solve2((blueprint, ore_robs + 1, clay_robs, ob_robs, geo_robs, min(new_ore - a, ore_cap), min(new_clay, clay_cap), min(new_ob, ob_cap), time - 1))
        sol = max(sol, pos_sol)

    if not geo_build or (ob_robs < f and (ore < c or clay < d)) or (clay_robs < d and (ore < b)) and (ore_robs < max(a, b, c, e) and (ore < a)):
        pos_sol = solve2((blueprint, ore_robs, clay_robs, ob_robs, geo_robs, min(new_ore, ore_cap), min(new_clay, clay_cap), min(new_ob, ob_cap), time - 1))
        sol = max(sol, pos_sol)

    m2[inp] = sol + geo_robs

    if len(m2) % 100000 == 0:
        print(len(m2))

    return m2[inp]

def p2(raw, lines, sections, nums, *args, **kwargs):
    global m2
    m2 = {}
    ans = 0

    blueprints = []
    for line in lines:
        _, a = line.split(': ')
        b = a.split('. ')

        c = b[0].split('costs ')
        c = int(c[1].split(' ')[0])

        d = b[1].split('costs ')
        d = int(d[1].split(' ')[0])

        e = b[2].split('costs ')[1]
        e = e.split(' ')
        e, f = int(e[0]), int(e[3])

        g = b[3].split('costs ')[1]
        g = g.split(' ')
        g, h = int(g[0]), int(g[3])

        blueprints.append((c, d, (e, f), (g, h)))

    ans = 1
    for b in blueprints[:3]:
        m2 = {}
        sol = solve2((b, 1, 0, 0, 0, 0, 0, 0, 32))
        print('SOL', sol)
        ans *= sol

    return ans

run_solutions(p1, p2)
