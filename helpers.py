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

