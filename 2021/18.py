import re
import sys
import argparse
import math

from collections import defaultdict, Counter

import sys
sys.path.append('../')

from executor import *
from helpers import *
from itertools import permutations

class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    @classmethod
    def from_list(cls, l, parent):
        val = None
        left = None
        right = None

        if type(l) is list:
            left = Node.from_list(l[0], None)
            right = Node.from_list(l[1], None)

            me = cls(val, left, right, parent)
            left.parent = me
            right.parent = me

            return me
        else:
            val = l

            me = cls(val, left, right, parent)

            return me

    def find_four(self, depth):
        if self.val is not None:
            return None

        elif depth == 4:
            return self

        explode_l = self.left.find_four(depth + 1)

        if explode_l is not None:
            return explode_l

        explode_r = self.right.find_four(depth + 1)

        if explode_r is not None:
            return explode_r

    def add_right(self, prev, num):
        # First, find the root at which we are a left child
        root = self

        while root.right is prev:
            prev = root
            root = root.parent

            if root is None:
                return None

        # Then find the leftmost child in the right subtree
        down = root.right

        while True:
            if down.val is not None:
                down.val += num
                break

            elif down.left is not None:
                down = down.left
                continue

            else:
                down = down.right

    def add_left(self, prev, num):
        root = self

        while root.left is prev:
            prev = root
            root = root.parent

            if root is None:
                return None

        down = root.left

        while True:
            if down.val is not None:
                down.val += num
                break

            elif down.right is not None:
                down = down.right
                continue

            else:
                down = down.left

    def find_split(self):
        if self.val is not None and self.val >= 10:
            return self

        if self.left is not None:
            l = self.left.find_split()

            if l is not None:
                return l

        if self.right is not None:
            r = self.right.find_split()

            if r is not None:
                return r

        return None

    def mag(self):
        if self.val is not None:
            return self.val

        l = 0
        r = 0

        if self.left is not None:
            l = self.left.mag()

        if self.right is not None:
            r = self.right.mag()

        return 3 * l + 2 * r

    def simplify(self):
        changed = True

        while changed:
            changed = False

            explode = self.find_four(0)

            if explode is not None:
                left = explode.left.val
                right = explode.right.val

                explode.parent.add_right(explode, right)
                explode.parent.add_left(explode, left)

                explode.left = None
                explode.right = None
                explode.val = 0

                changed = True
                continue

            split = self.find_split()

            if split is not None:
                new_l = math.floor(split.val/2)
                new_r = math.ceil(split.val/2)

                split.val = None
                split.left = Node(new_l, None, None, split)
                split.right = Node(new_r, None, None, split)

                changed = True

def p1(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    curr_tree = None

    for line in lines:
        inp = eval(line)
        new_root = Node.from_list(inp, None)

        if curr_tree is None:
            curr_tree = new_root

        else:
            new = Node(None, curr_tree, new_root, None)
            curr_tree.parent = new
            new_root.parent = new

            curr_tree = new

        curr_tree.simplify()

        changed = True

    ans = curr_tree.mag()

    return ans

def p2(raw, lines, sections, nums, *args, **kwargs):
    ans = 0

    for first, second in permutations(lines, 2):
        curr_tree = None
        inps = [first, second]
        for line in inps:
            inp = eval(line)
            new_root = Node.from_list(inp, None)

            if curr_tree is None:
                curr_tree = new_root

            else:
                new = Node(None, curr_tree, new_root, None)
                curr_tree.parent = new
                new_root.parent = new

                curr_tree = new

            curr_tree.simplify()

            ans = max(ans, curr_tree.mag())

    return ans

run_solutions(p1, p2)
