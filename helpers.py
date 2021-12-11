import re
from collections import defaultdict

def section_to_matrix(section):
    '''
    Converts a series of lines with space-separated integers
    into a 2D list
    '''

    return [[int(n) for n in line.split()] for line in section]

def transpose(matrix):
    '''
    Computes the transpose of a matrix
    '''

    output = []

    for i in range(len(matrix[0])):
        row = [matrix[j][i] for j in range(len(matrix))]

        output.append(row)

    return output

def create_matrix(width, height, value):
    matrix = []

    for i in range(height):
        row = []

        for j in range(width):
            row.append(value)

        matrix.append(row)

    return matrix

def drange(start, stop):
    '''
    Produces a range from start to stop, inclusive, with a step of 1 in the
    appropriate direction
    '''

    if start < stop:
        return range(start, stop + 1)

    else:
        return range(start, stop - 1, -1)

def get_regex_groups(pattern, string):
    return re.search(pattern, string).groups()

def stoil(l):
    '''
    Converts a list of strings to a list of ints
    '''

    return list(map(int, l))

def count_freq(l):
    '''
    Produces a dictionary with the number each element appears in the list
    '''

    freq = defaultdict(int)

    for element in l:
        freq[element] += 1

    return freq

class Grid:
    '''
    A helper class to encapsulate all the annoying 2D grid stuff
    '''

    def __init__(self, content):
        self.content = content
        self.width = len(content[0])
        self.height = len(content)

    def valid(self, row, col):
        return 0 <= row <= self.height - 1 and 0 <= col <= self.width - 1

    def get(self, row, col):
        if not self.valid(row, col):
            return None # Should we raise an exception? Or let this happen?

        return self.content[row][col]

    def get_adj4(self, row, col):
        '''
        Returns the set of all valid rows and columns of the four adjacent cells
        '''

        possible = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        return [p for p in possible if self.valid(*p)]

    def get_adj8(self, row, col):
        '''
        Returns a list of vallid valid rows and columsn in the eight adjacent cells
        '''

        possible = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]

        return [p for p in possible if self.valid(*p)]

