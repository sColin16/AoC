import argparse
import sys
import os

from aoc_parser import *

def get_flags():
    '''
    Retrieves flags to determine settings
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", nargs="?", default="a")     # Specify which inputs to run on
    parser.add_argument("part", nargs="?", default='all')   # Specify 1 or 2

    return parser.parse_args()

def get_settings(flags):
    '''
    Parses the flags to determine the settings to run in
    '''
    
    abbrv_map = {
        'a': 'all',
        'e': 'example',
        'm': 'manual',
        'r': 'repeat'
    }

    settings = {
        'mode': abbrv_map[flags.mode],
        'part': 'all' if flags.part == 'all' else int(flags.part)
    }

    return settings

def get_day():
    '''
    Determines day of the problem being executed (to pull associated input files)
    '''

    return int(sys.argv[0].split('.')[0])

flags = get_flags()
settings = get_settings(flags)
day = get_day()

def run_solutions(p1, p2):
    '''
    Handles executing the solutions to the parts, passing in inputs for any and
    all test cases that we wish to be executed
    '''

    texts = {}

    if settings['mode'] == 'example' or settings['mode'] == 'all':
        texts['example'] = read_file(f'{day}-example.txt')

    if settings['mode'] == 'all':
        texts['input'] = read_file(f'{day}-input.txt')

    if settings['mode'] == 'repeat':
        texts['repeat'] = read_file(f'{day}-manual.txt')

    if settings['mode'] == 'manual':
        manual_text = read_stdin()
        texts['manual'] = manual_text

        with open(f'{day}-manual.txt', 'w') as f:
            f.write(manual_text)
            f.write('\n')

    for (mode, text) in texts.items():
        parsed = parse_text(text)

        if settings['part'] == 1 or settings['part'] == 'all':
            result1 = p1(**parsed)

            print(f'{mode} part 1: {result1}')

        if settings['part'] == 2 or settings['part'] == 'all':
            result2 = p2(**parsed)

            print(f'{mode} part 2: {result2}')

