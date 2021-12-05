import re

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

def stoi_list(l):
    return list(map(int, l))

