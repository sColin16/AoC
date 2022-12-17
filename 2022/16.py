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

from typing import List
from dataclasses import dataclass

import itertools

import heapq

@dataclass
class Node:
    label: str
    rate: int
    children: List[str]
    achildren: List[str]

hits = 0
def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    graph = {}
    pres = {}
    comp_nodes = ['AA']
    for line in lines:
        label = line.split(' ')[1]
        rate = int(line.split('=')[1].split(';')[0])
        if ',' in line:
            valves = line.split('valves ')[1].split(', ')
        else:
            valves = line.split('valve ')[1].split(', ')

        graph[label] = Node(label, rate, valves, valves + [label])

        if rate > 0:
            pres[label] = rate
            comp_nodes.append(label)

    comp_graph = {}

    for start in comp_nodes:
        q = set([(start, 0)])
        visited = set([start])
        leaves = []

        while len(q) > 0:
            node, distance = q.pop()
            if graph[node].rate > 0 and node != start:
                leaves.append((node, distance))

            for child in graph[node].children:
                if child not in visited:
                    q.add((child, distance + 1))
                    visited.add(child)

        comp_graph[start] = Node(start, graph[start].rate, leaves, leaves + [(start, 0)])

    m = {}
    def solve(inp):
        if inp in m:
            return m[inp]
        node, activated, tleft = inp

        if tleft == 0:
            return 0

        best = 0

        if graph[node].rate > 0 and node not in activated:
            nset = set(activated)
            nset.add(node)

            next_sol = solve((node, frozenset(nset), tleft - 1))
            cand_val = (graph[node].rate) * (tleft - 1) + next_sol

            best = max(best, cand_val)

        for neighbor, d in comp_graph[node].children:
            if tleft >= d:
                best = max(best, solve((neighbor, activated, tleft - d)))

        m[inp] = best
        return m[inp]

    ans = solve(('AA', frozenset(), 30))
    print(len(m))

    return ans

    # q = []
    # processed = set()
    # heapq.heappush(q, (0, ('AA', frozenset(), 30)))
    # best = defaultdict(int)
    # best[('AA', frozenset(), 30)] = 0

    # while len(q) > 0:
    #     cost, state = heapq.heappop(q)
    #     node, activated, t_left = state
    #     value = best[state]

    #     if state in processed:
    #         continue

    #     if t_left == 0:
    #         return best[state]

    #     processed.add(state)

    #     # Check releasing this valve, if the pressure is non-zero
    #     if node not in activated and graph[node].rate > 0:
    #         new_set = set(activated)
    #         new_set.add(node)
    #         new_set = frozenset(new_set)

    #         # neighbor = (node, new_set, t_left - 1, value + (graph[node].rate) * (t_left - 1))
    #         neighbor = (node, new_set, t_left - 1)
    #         best[neighbor] = max(best[neighbor], value + (graph[node].rate) * (t_left - 1))

    #         if neighbor not in processed:
    #             new_cost = 0
    #             for n in pres:
    #                 if n not in new_set:
    #                     new_cost += graph[n].rate

    #             heapq.heappush(q, (cost + new_cost, neighbor))

    #     # Check moving to all our neighbors, which have the same cost
    #     new_cost = 0
    #     for n in pres:
    #         if n not in activated:
    #             new_cost += graph[n].rate

    #     for nnode in graph[node].children:
    #         neighbor = (nnode, activated, t_left - 1)

    #         best[neighbor] = max(best[neighbor], value)

    #         if neighbor not in processed:
    #             heapq.heappush(q, (cost + new_cost, neighbor))

    # return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    graph = {}
    pres = {}
    comp_nodes = ['AA']
    pres_index = {}
    for line in lines:
        label = line.split(' ')[1]
        rate = int(line.split('=')[1].split(';')[0])
        if ',' in line:
            valves = line.split('valves ')[1].split(', ')
        else:
            valves = line.split('valve ')[1].split(', ')

        graph[label] = Node(label, rate, valves, valves + [label])

        if rate > 0:
            pres[label] = rate
            comp_nodes.append(label)
            pres_index[label] = len(pres_index)

    comp_graph = {}

    for start in comp_nodes:
        q = set([(start, 0)])
        visited = set([start])
        leaves = []

        while len(q) > 0:
            node, distance = q.pop()
            if graph[node].rate > 0 and node != start:
                leaves.append((node, distance))

            for child in graph[node].children:
                if child not in visited:
                    q.add((child, distance + 1))
                    visited.add(child)

        comp_graph[start] = Node(start, graph[start].rate, leaves, leaves + [(start, 0)])

    m = {}
    def solve(inp):
        if inp in m:
            return m[inp]

        n1, n2, activated, t1, t2 = inp

        if t1 == 0 and t2 == 0:
            return 0

        n1_active = (activated >> pres_index[n1]) & 1
        n2_active = (activated >> pres_index[n2]) & 1

        # print(n1_active, n2_active)

        best = 0

        # Simulate n2 moving
        if t2 > 0 and not n2_active:
            nset = activated + (1 << pres_index[n2])
            value = (graph[n2].rate) * (t2 - 1)

            if nset == 2 ** (len(pres_index)) - 1:
                best = max(best, value)

            else:
                found = 0
                for neighbor, d in comp_graph[n2].children:
                    if not ((nset >> pres_index[neighbor]) & 1) and n1 != neighbor:
                        found += 1
                        next_sol = solve((n1, neighbor, nset, t1, max(0, t2 - 1 - d)))
                        cand_val = value + next_sol
                        best = max(best, cand_val)

                # This isn't right, it's possible 2 should take it
                if found == 0:
                    next_sol = solve((n1, n2, nset, t1, 0))
                    cand_val = value + next_sol
                    best = max(best, cand_val)


        # Simulate n1 moving
        if t1 > 0 and not n1_active:
            nset = activated + (1 << pres_index[n1])
            value = (graph[n1].rate) * (t1 - 1)

            if nset == 2 ** (len(pres_index)) - 1:
                best = max(best, value)

            else:
                found = 0
                for neighbor, d in comp_graph[n1].children:
                    if not ((nset >> pres_index[neighbor]) & 1) and n2 != neighbor:
                        found += 1
                        next_sol = solve((neighbor, n2, nset, max(0, t1 - 1 - d), t2))
                        cand_val = value + next_sol
                        best = max(best, cand_val)

                if found == 0:
                    next_sol = solve((n1, n2, nset, 0, t2))
                    cand_val = value + next_sol
                    best = max(best, cand_val)

        m[inp] = best
        if len(m) % 10000 == 0:
            print(len(m))
        return m[inp]

        # if t1 >= 1 and t2 >= 1 and not n1_active and not n2_active and n1 != n2:
        #     nset = activated + (1 << pres_index[n1]) + (1 << pres_index[n2])

        #     next_sol = solve((n1, n2, nset, t1 - 1, t2 - 1))
        #     value = (graph[n1].rate) * (t1 - 1) + (graph[n2].rate) * (t2 - 1)
        #     cand_val = value + next_sol

        #     best = max(best, cand_val)

        # if t1 >= 1 and not n1_active:
        #     nset = activated + (1 << pres_index[n1])

        #     value = (graph[n1].rate) * (t1 - 1)

        #     for neighbor, d in comp_graph[n2].children:
        #         next_sol = solve((n1, neighbor, nset, t1 - 1, max(0, t2 - d)))
        #         cand_val = value + next_sol
        #         best = max(best, cand_val)

        # if t2 >= 1 and not n2_active:
        #     nset = activated + (1 << pres_index[n2])

        #     value = (graph[n2].rate) * (t2 - 1)

        #     for neighbor, d in comp_graph[n1].children:
        #         next_sol = solve((neighbor, n2, nset, max(0, t1 - d), t2 - 1))
        #         cand_val = value + next_sol
        #         best = max(best, cand_val)

        # for (neighbor1, d1), (neighbor2, d2) in itertools.product(comp_graph[n1].children, comp_graph[n2].children):
        #     best = max(best, solve((neighbor1, neighbor2, activated, max(0, t1 - d1), max(0, t2 - d2))))



    # ans = solve(('AA', 'AA', frozenset(), 26, 26))
    ans = 0
    for (n1, d1), (n2, d2) in itertools.product(comp_graph['AA'].children, comp_graph['AA'].children):
        if n1 != n2:
            ans = max(ans, solve((n1, n2, 0, 26 - d1, 26 - d2)))
    print(hits)
    print(len(m))

    return ans

        # for neighbor, d in comp_graph[n1].achildren:
        #     if d == 0:
        #         if t1 < 1:
        #             continue

        #         if neighbor not in activated:
        #             nset = set(activated)
        #             nset.add(neighbor)
        #             best = max(best, (graph[neighbor].rate) * (t1 - 1) + solve((neighbor, n2, frozenset(nset), t1 - 1, t2)))

        #         else:
        #             continue
        #             # best = max(best, solve((neighbor, n2, activated, t1 - 1, t2)))

        #     else:
        #         if t1 < d:
        #             continue

        #         best = max(best, solve((neighbor, n2, activated, t1 - d, t2)))

        # for neighbor, d in comp_graph[n2].achildren:
        #     if d == 0:
        #         if t2 < 1:
        #             continue

        #         if neighbor not in activated:
        #             nset = set(activated)
        #             nset.add(neighbor)
        #             best = max(best, (graph[neighbor].rate) * (t2 - 1) + solve((n1, neighbor, frozenset(nset), t1, t2 - 1)))

        #         else:
        #             continue
        #             # best = max(best, solve((n1, neighbor, activated, t1, t2 - 1)))

        #     else:
        #         if t2 < d:
        #             continue

        #         best = max(best, solve((n1, neighbor, activated, t1, t2 - d)))


        # m[inp] = best
        # if len(m) % 10000 == 0:
        #     print(len(m))

        # return m[inp]

    return solve(('AA', 'AA', frozenset(), 26, 26))

    q = []
    processed = set()
    heapq.heappush(q, (0, ('AA', 'AA', frozenset(), 26, 26)))
    best = defaultdict(int)
    best[('AA', 'AA', frozenset(), 26, 26)] = 0

    z = 0
    y = 26
    while len(q) > 0:
        cost, state = heapq.heappop(q)
        node1, node2, activated, t_left1, t_left2 = state
        value = best[state]

        if len(q) % 10000 == 0:
            print(len(q))

        if state in processed:
            continue

        if (t_left1 == 0 and t_left2 == 0):
            return best[state]

        processed.add(state)

        # p = set(itertools.product(graph[node1].achildren, graph[node2].achildren))
        # p = set((n1, n2) if n1 < n2 else (n2, n1) for n1, n2 in p)

        for nnode1, d1 in comp_graph[node1].achildren:
            new_set = set(activated)
            new_val = value
            new_cost = 0

            if d1 == 0:
                new_tleft1 = t_left1 - 1

                if nnode1 not in new_set:
                    new_set.add(nnode1)
                    new_val += (graph[nnode1].rate) * (t_left1 - 1)

                for n in pres:
                    if n not in new_set:
                        new_cost += graph[n].rate

            elif d1 > 0:
                new_tleft1 = t_left1 - d1

                for n in pres:
                    if n not in new_set:
                        new_cost += graph[n].rate * d1

            if new_tleft1 < 0:
                continue

            fnew = frozenset(new_set)
            neighbor = (nnode1, node2, fnew, new_tleft1, t_left2)
            best[neighbor] = max(best[neighbor], new_val)

            if neighbor not in processed:
                heapq.heappush(q, (cost + new_cost, neighbor))

        for nnode2, d2 in comp_graph[node2].achildren:
            new_set = set(activated)
            new_val = value
            new_cost = 0

            if d2 == 0:
                new_tleft2 = t_left2 - 1

                if nnode2 not in new_set:
                    new_set.add(nnode2)
                    new_val += (graph[nnode2].rate) * (t_left2 - 1)

                for n in pres:
                    if n not in new_set:
                        new_cost += graph[n].rate

            elif d2 > 0:
                new_tleft2 = t_left2 - d2

                for n in pres:
                    if n not in new_set:
                        new_cost += graph[n].rate * d2

            if new_tleft2 < 0:
                continue

            fnew = frozenset(new_set)
            neighbor = (node1, nnode2, fnew, t_left1, new_tleft2)
            best[neighbor] = max(best[neighbor], new_val)

            if neighbor not in processed:
                heapq.heappush(q, (cost + new_cost, neighbor))
        # for nnode1, nnode2 in children[(node1, node2)]:
        # for (nnode1, d1), (nnode2, d2) in itertools.product(comp_graph[node1].achildren, comp_graph[node2].achildren):
        #     # if d1 > t_left1 or d2 > t_left2:
        #     #     continue

        #     new_set = set(activated)
        #     new_val = value
        #     new_cost = 0

        #     if d1 == 0:
        #         new_tleft1 = t_left1 - 1

        #         if nnode1 not in new_set:
        #             new_set.add(nnode1)
        #             new_val += (graph[nnode1].rate) * (t_left1 - 1)

        #         for n in pres:
        #             if n not in new_set:
        #                 new_cost += graph[n].rate

        #     elif d1 > 0:
        #         new_tleft1 = t_left1 - d1

        #         for n in pres:
        #             if n not in new_set:
        #                 new_cost += graph[n].rate * d1

        #     if d2 == 0:
        #         new_tleft2 = t_left2 - 1

                # if nnode2 not in new_set:
                #     new_set.add(nnode2)
                #     new_val += (graph[nnode2].rate) * ( t_left2 - 1)

                # for n in pres:
                #     if n not in new_set:
                #         new_cost += graph[n].rate

            # elif d2 > 0:
                # new_tleft2 = t_left2 - d2

                # for n in pres:
                #     if n not in new_set:
                #         new_cost += graph[n].rate * d2

            # if new_tleft1 < 0 or new_tleft2 < 0:
                # continue

            # if nnode1 == node1 and nnode1 not in new_set and graph[nnode1].rate > 0:
            #     new_set.add(nnode1)
            #     new_val += (graph[nnode1].rate) * (t_left - 1)

            # if nnode2 == node2 and nnode2 not in new_set and graph[nnode2].rate > 0:
            #     new_set.add(nnode2)
            #     new_val += (graph[nnode2].rate) * (t_left - 1)

            # fnew = frozenset(new_set)
            # neighbor = (nnode1, nnode2, fnew, new_tleft1, new_tleft2)
            # best[neighbor] = max(best[neighbor], new_val)

            # if neighbor not in processed:
            #     heapq.heappush(q, (cost + new_cost, neighbor))

    return ans

run_solutions(p1, p2)
