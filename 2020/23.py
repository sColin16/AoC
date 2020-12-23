import re
import sys
import argparse
import math

from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-r", "--repeat_test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

    with open('23-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('23-test.txt', 'r').read().strip()

else:
    raw = open('23-input.txt', 'r').read().strip()

lines = raw.split('\n')
sections = [section.split('\n') for section in raw.split('\n\n')]

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

cups = [int(num) for num in list(raw)]
cup_num = max(cups)

current_cup = cups[0]
print(cups)
for i in range(100):
    current_idx = cups.index(current_cup)
    remove_idxs = [] 
    for i in range(3):
        idx = (current_idx + 1 + i) % cup_num
        remove_idxs.append(idx)

    remove = [cups[idx] for idx in remove_idxs]

    for r in remove:
        cups.remove(r)

    destination = current_cup

    while True:
        destination = (destination + cup_num) % cup_num - 1

        if destination == 0:
            destination = cup_num

        elif destination == -1:
            destination = cup_num - 1

        if destination not in remove:
            break

    dest_idx = cups.index(destination)

    for cup in reversed(remove):
        cups.insert(dest_idx+1, cup)

    current_cup = cups[(cups.index(current_cup) + 1) % cup_num]

while cups[0] != 1:
    cups.append(cups.pop(0))

ans = ''.join([str(cup) for cup in cups])[1:]

print('Part 1:', ans)

###########################

class LNode:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

nodes = {}

# Part 2
ans = 0

cups = [int(num) for num in list(raw)]

first = LNode(None, None, cups[0])
f_cups = first
b_cups = first
nodes[cups[0]] = first

for c in cups[1:]:
    new = LNode(b_cups, None, c)
    b_cups.right = new
    b_cups = new

    nodes[c] = new

for c in range(max(cups) + 1, 1000001):
    new = LNode(b_cups, None, c)
    b_cups.right = new
    b_cups = new

    nodes[c] = new

f_cups.left = b_cups
b_cups.right = f_cups

cup_num = 1000000

current_cup = f_cups

for i in tqdm(range(10000000)):
    remove = []

    for i in range(3):
        remove.append(current_cup.right)
        current_cup.right = current_cup.right.right
        current_cup.right.left = current_cup

    p = f_cups

    destination = current_cup.value

    while True:
        destination -= 1

        if destination == 0:
            destination = cup_num

        elif destination == -1:
            destination = cup_num - 1

        if destination not in [v.value for v in remove]:
            break

    d_node = nodes[destination]

    for cup in reversed(remove):
        cup.left = d_node
        cup.right = d_node.right
        d_node.right.left = cup
        d_node.right = cup

    current_cup = current_cup.right

p = f_cups
for i in range(10):
    print(p.value)
    p = p.right

print(nodes[1].right.value, nodes[1].right.right.value)
ans = nodes[1].right.value * nodes[1].right.right.value
print('Part 2:', ans)
