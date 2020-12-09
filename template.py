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

def execute_loop(commands, loop_terminate=True):
    '''
    Executes lines of commands, as per the day 8 problem. If loop_terminate is
    True, will terminate once an instruction is to be run a second time. If
    loop_teriminate if false, will terminate once the program jumps to command
    index after the final command.
    '''

    i = 0
    acc = 0
    run = set()

    while True:
        if loop_terimnate and i in run:
            return acc

        if not loop_terminate and i == len(commands):
            return acc

        run.add(i)
        command, num = commands[i].split()
        num = int(num)

        if command == 'nop':
            i += 1

        elif command == 'acc':
            acc += num
            i += 1

        elif command == 'jmp':
            i += num

# Part 1
ans = 0

#START

print('Part 1:', ans)

###########################

# Part 2
ans = 0



print('Part 2:', ans)
