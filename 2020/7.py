import re
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

else:
    raw = open('7-input.txt', 'r').read().strip()

lines = raw.split('\n')

# Part 1
ans = -1

container_dict = {}

for line in lines:
    line = line[:-1]
    container = line[:line.index('bag')-1]
    inner_str = line[line.index('contain')+8:]
    inner_bags = [string[2:-4].strip() for string in inner_str.split(', ')]

    if inner_str != "no other bags":
        for bag in inner_bags:
            if bag not in container_dict:
                container_dict[bag] = []
            container_dict[bag].append(container)

queue = ['shiny gold']
bags = set()

while len(queue) != 0:
    next_bag = queue.pop(0)
    bags.add(next_bag)

    if next_bag in container_dict:
        for val in container_dict[next_bag]:
            queue.append(val)

ans = len(bags) - 1

print('Part 1:', ans)

###########################

# Part 2
ans = 0

contained_dict = {}

for line in lines:
    line = line[:-1]
    container = line[:line.index('bag')-1]
    inner_str = line[line.index('contain')+8:]
    inner_bags = [string[2:-4].strip() for string in inner_str.split(', ')]
    if inner_str != "no other bags":
        counts = [int(string[0]) for string in inner_str.split(', ')]

        contained_dict[container] = list(zip(inner_bags, counts))

queue = ['shiny gold']

while len(queue) != 0:
    next_bag = queue.pop(0)
    if next_bag in contained_dict:
        contained = contained_dict[next_bag]

        for bag in contained:
            ans += bag[1]

            for i in range(bag[1]):
                queue.append(bag[0])

print('Part 2:', ans)
