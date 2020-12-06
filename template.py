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
    raw = open('xx-input.txt', 'r').read().strip()

lines = raw.split('\n')

# Part 1
ans = 0



print('Part 1:', ans)

###########################

# Part 2
ans = 0



print('Part 2:', ans)
