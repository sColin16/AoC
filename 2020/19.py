import re
import sys
import argparse
import itertools
import math
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-r", "--repeat_test", action="store_true")
args = parser.parse_args()

if args.test:
    raw = sys.stdin.read().strip()

    with open('19-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('19-test.txt', 'r').read().strip()

else:
    raw = open('19-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

# Input parsing
rules, messages = raw.split('\n\n')
rules = rules.split('\n')
messages = messages.split('\n')

r_dict = {}

for rule in rules:
    col_idx = rule.index(':')

    num = int(rule[:col_idx])
    parts = rule[col_idx+2:]

    if '"' in parts:
        p = parts[1]

    else:
        options = parts.split(' | ')
        p = []
        for option in options:
            p.append([int(num) for num in option.split(' ')])

    r_dict[num] = p

# Returns a list of all possible strings that match a given rule number
def possible(rule):
    # Base case: rule is just the letter a or b
    if type(r_dict[rule]) == str and r_dict[rule] in 'ab':
        return [r_dict[rule]]

    # Find possible strings for each option of the rule
    p = []
    for option in r_dict[rule]:
        # Get all possible strings for each element of the rule
        a = []
        for num in option:
            a.append(possible(num))

        # Use the product function to combine them, then join them into individual strings
        a = list(itertools.product(*a))
        a = [''.join(t) for t in a]

        p.extend(a)

    return p

# Because there are no loops, the rule set is small enough that we can generate
# the entire space of valid strings, then check to see if each message is valid

valid = set(possible(0))

for m in messages:
    if m in valid:
        ans += 1

print('Part 1:', ans)

###########################

# Part 2
ans = 0

# The final rule ends up being "{m * 42} {n * 42} {n * 31}" where n and m are
# some unknown positive integers, which makes the problem hard. 

# Thus, all we care about are the valid strings for rules 42 and 31
four2 = possible(42)
three1 = possible(31)

final = set()

# All possible valid strings in 42 and 31 have the convenient property of being
# the same length, so we just have to check blocks of that length to check if a
# string is valid
size = len(four2[0])

for msg in messages:
    # Check for first blocks to see if they match rule 42 (but leave room for n=1)
    for i in range(int((len(msg) - 2 * size) / size)):
        if msg[i * size: (i + 1) * size] in four2:
            # Get the rest of the string after the initial rule 42 is verified
            half = msg[(i + 1) * size:]

            # Determine "n", make sure n is an integer (not x.5, which is possible)
            augment = (len(half) / size / 2)
            
            if abs(int(augment) - augment) > 0.0001:
                continue

            augment = int(augment)

            # Check that the first n blocks follow rule 42
            valid = True
            for i in range(augment):
                if half[i * size:(i + 1) * size] not in four2:
                    valid = False
                    break

            # Check that the second set of n blocks follow rule 31
            if valid:
                for i in range(augment):
                    if half[(augment + i) * size: (augment + i + 1) * size] not in three1:
                        valid = False
                        break

            # Add the message to the set if its valid, stop checking that message
            if valid:
                final.add(msg)
                break

        else:
            break

ans = len(final)

print('Part 2:', ans)
