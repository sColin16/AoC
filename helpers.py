import re
from collections import defaultdict
from queue import SimpleQueue, PriorityQueue

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

def dmatrix(lines):
    '''
    Converts a grid of digits into a 2D list of integers
    '''

    return [stoil(list(line)) for line in lines]

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

    def __repr__(self):
        return '\n'.join([str(row) for row in self.content])

def flood_fill(start_node, get_neighbors, hashable_transform=lambda x: x):
    '''
    Returns a dictionary of the distance to all connected nodes
    Assumes an unweighted graph

    start_node is a representation of the node to start at
    get_neighbors is a callback that is passed a node and should return all valid neighrbors
    hashable_transform is a callback to transform a node into a hashable type, if necessary
    '''

    hashable_start = hashable_transform(start_node)

    q = SimpleQueue()

    q.put((start_node, 0))
    visited = set([hashable_start])
    distances = {
        hashable_start: 0
    }

    while q.qsize() > 0:
        node, distance = q.get()

        for neighbor in get_neighbors(node):
            hashable_neighbor = hashable_transform(neighbor)

            if hashable_neighbor not in visited:
                q.put((neighbor, distance + 1))
                visited.add(hashable_transform(neighbor))
                distances[hashable_neighbor] = distance + 1

    return distances

def dijsktras(start_node, target_node, get_neighbors, hashable_transform=lambda x: x):
    '''
    Returns the minimum cost to reach the target node from the start node

    get_neighbors should return a list of (node, cost) tuples
    '''

    hashable_start = hashable_transform(start_node)

    q = PriorityQueue()
    processed = set()

    # Store the hash in case there are collisions with distance
    q.put((0, hash(hashable_start), start_node))

    while q.qsize() > 0:
        distance, h, node = q.get()

        hashable_node = hashable_transform(node)

        if hashable_node in processed:
            continue

        if node == target_node:
            return distance

        processed.add(hashable_node)

        for neighbor, cost in get_neighbors(node):
            hashable_neighbor = hashable_transform(neighbor)

            if hashable_neighbor not in processed:
                q.put((distance + cost, hash(hashable_neighbor), neighbor))

    return None

