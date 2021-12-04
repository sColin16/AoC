import sys

def read_stdin():
    return sys.stdin.read().strip()

def read_file(path):
    return open(path, 'r').read().strip()

def parse_text(text):
    lines = text.split('\n')
    sections = [section.split('\n') for section in text.split('\n\n')]

    try:
        nums = [int(line) for line in lines]
    except Exception as e:
        nums = None

    return {
        'raw': text,
        'lines': lines,
        'sections': sections,
        'nums': nums
    }

