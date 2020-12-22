import re
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-r", "--repeat_test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

    with open('22-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('22-test.txt', 'r').read().strip()

else:
    raw = open('22-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

p1, p2 = raw.split('\n\n')
p1 = [int(num) for num in p1.split('\n')[1:]]
p2 = [int(num) for num in p2.split('\n')[1:]]

while len(p1) > 0 and len(p2) > 0:
    c1 = p1.pop(0)
    c2 = p2.pop(0)

    if c1 > c2:
        p1.append(c1)
        p1.append(c2)

    elif c2 > c1:
        p2.append(c2)
        p2.append(c1)

c = []
if len(p1) > 0:
    c = p1

else:
    c = p2

for i in range(len(c)):
    ans += (len(c) - i) * c[i]

print('Part 1:', ans)

###########################

# Part 2
ans = 0


def play(p1, p2, d): 
    previous = set()

    while True:
        if len(p1) == 0 or len(p2) == 0:
            break

        if str(p1) + str(p2) in previous:
            return 1

        previous.add(str(p1) + str(p2))

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        winner = 0
        if c1 <= len(p1) and c2 <= len(p2):
            winner = play(p1[:c1], p2[:c2], d+1)

        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            p1.append(c1)
            p1.append(c2)

        elif winner == 2:
            p2.append(c2)
            p2.append(c1)

    if len(p1) == 0:
        return 2

    elif len(p2) == 0:
        return 1

p1, p2 = raw.split('\n\n')
p1 = [int(num) for num in p1.split('\n')[1:]]
p2 = [int(num) for num in p2.split('\n')[1:]]

print(play(p1, p2, 0))
print(p1)
print(p2)

ans = 0
c = []
if len(p1) > 0:
    c = p1

else:
    c = p2

print(c)

for i in range(len(c)):
    ans += (len(c) - i) * c[i]

print('Part 2:', ans)
