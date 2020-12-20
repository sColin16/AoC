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

    with open('20-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('20-test.txt', 'r').read().strip()

else:
    raw = open('20-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

tiles = raw.split('\n\n')

# top, bottom, left, right
t_dict = {}
t_dict2 = {}

for tile in tiles:
    tile = tile.split('\n')

    num = int(tile[0][5:9])
    tile = tile[1:]

    for i, line in enumerate(tile):
        tile[i] = line.replace('#', '1').replace('.', '0')

    top = tile[0]
    bottom = tile[9]
    left = ''.join([t[0] for t in tile])
    right = ''.join([t[9] for t in tile])

    t_dict[num] = [[int(top, 2), int(top[::-1], 2)], [int(bottom, 2),
        int(bottom[::-1], 2)], [int(left, 2), int(left[::-1], 2)], [int(right,
            2), int(right[::-1], 2)]]

    t_dict2[num] = tile

counts = {}

for t in t_dict:
    for l in t_dict[t]:
        if l[0] in counts:
            counts[l[0]] += 1
        else:
            counts[l[0]] = 1

        if l[1] in counts:
            counts[l[1]] += 1
        else:
            counts[l[1]] = 1


matches = set()
for key, value in counts.items():
    if value == 2:
        matches.add(key)

ans = 1
corners = []
for k, v in t_dict.items():
    a = 0
    for i in range(len(v)):
        if v[i][0] in matches:
            a += 1

    if a == 2:
        corners.append(k)
        ans *= k

print('Part 1:', ans)

###########################

# Part 2
ans = 0


def remove_border(tile):
    new = []

    for i in range(1, len(tile) - 1):
        new.append(tile[i][1:-1])

    return new

# Rotate 90 degrees counterclockwise
def rotate(tile):
    new = []
    for i in range(len(tile)):
        new.append([0] * len(tile))

    for i in range(len(tile)):
        for j in range(len(tile)):
            new[len(tile) - j - 1][i] = tile[i][j]

    for i, line in enumerate(new):
        new[i] = ''.join(line)

    return new

def flip_vertical(tile):
    new = tile[:][:]

    for i in range(len(new)):
        new[i] = new[i][::-1]

    return new

def flip_horizontal(tile):
    new = tile[:][:]

    for i in range(int(len(tile) / 2)):
        temp = new[i]
        new[i] = new[len(tile) - i - 1]
        new[len(tile) - i - 1] = temp

    return new

def rotate_id(i):
    t_dict2[i] = rotate(t_dict2[i])
    t_dict[i] = [t_dict[i][3], t_dict[i][2], t_dict[i][0], t_dict[i][1]]

    t_dict[i][2] = [t_dict[i][2][1], t_dict[i][2][0]]
    t_dict[i][3] = [t_dict[i][3][1], t_dict[i][3][0]]

def flip_id_v(i):
    t_dict2[i] = flip_vertical(t_dict2[i])
    t_dict[i] = [t_dict[i][0], t_dict[i][1], t_dict[i][3], t_dict[i][2]]

    t_dict[i][0] = [t_dict[i][0][1], t_dict[i][0][0]]
    t_dict[i][1] = [t_dict[i][1][1], t_dict[i][1][0]]

def flip_id_h(i):
    t_dict2[i] = flip_horizontal(t_dict2[i])
    t_dict[i] = [t_dict[i][1], t_dict[i][0], t_dict[i][2], t_dict[i][3]]

    t_dict[i][2] = [t_dict[i][2][1], t_dict[i][2][0]]
    t_dict[i][3] = [t_dict[i][3][1], t_dict[i][3][0]]

first = t_dict[corners[0]]

if first[0][0] in matches:
    # rotate clockwise
    for i in range(3):
        rotate_id(corners[0])

elif first[1][0] in matches:
    # rotate counterclockwise
    rotate_id(corners[0])

elif first[2][0] in matches:
    # flip along vertical axis
    flip_id_v(corners[0])

grid = []
id_grid = []
side = int(math.sqrt(len(tiles)))
for i in range(side):
    grid.append([-1] * side)
    id_grid.append([-1] * side)

grid[0][0] = t_dict2[corners[0]]
id_grid[0][0] = corners[0]

placed = set()
placed.add(corners[0])

# Construct all the tile between the upper corners

find = t_dict[corners[0]][3][0]
for i in range(1, side - 1):
    for k, v in t_dict.items():
        if k in placed:
            continue
            
        if v[0][0] == find:
            # counterclockwise, horizontal flip
            rotate_id(k)

            flip_id_h(k)

        elif v[0][1] == find:
            # counterclockwise
            rotate_id(k)

        elif v[1][0] == find:
            # clockwise
            for j in range(3):
                rotate_id(k)

        elif v[1][1] == find:
            # clockwise, horizontal flip
            for j in range(3):
                rotate_id(k)
            flip_id_h(k)

        elif v[2][0] == find:
            # Do nothing
            pass

        elif v[2][1] == find:
            # horizontal
            flip_id_h(k)

        elif v[3][0] == find:
            # vertical
            flip_id_v(k)

        elif v[3][1] == find:
            # clockwise * 2
            for j in range(2):
                rotate_id(k)

        else:
            continue

        placed.add(k)
        grid[0][i] = t_dict2[k][:][:]
        id_grid[0][i] = k
        find = t_dict[k][3][0]

        break


# Construct the final corner
corners.pop(0)

for i in range(len(corners)):
    k = corners[i]
    v = t_dict[corners[i]]

    if v[0][0] == find:
        # counterclockwise, horizontal flip
        rotate_id(k)

        flip_id_h(k)

    elif v[0][1] == find:
        # counterclockwise
        rotate_id(k)

    elif v[1][0] == find:
        # clockwise
        for j in range(3):
            rotate_id(k)

    elif v[1][1] == find:
        # clockwise, horizontal flip
        for j in range(3):
            rotate_id(k)
        flip_id_h(k)

    elif v[2][0] == find:
        # Do nothing
        pass

    elif v[2][1] == find:
        # horizontal
        flip_id_h(k)

    elif v[3][0] == find:
        # vertical
        flip_id_v(k)

    elif v[3][1] == find:
        # clockwise * 2
        for j in range(2):
            rotate_id(k)

    else:
        continue

    corners.pop(i)
    placed.add(k)
    grid[0][side - 1] = t_dict2[k][:][:]
    id_grid[0][side - 1] = k
    break


# Fill in all the middle rows
for i in range(1, side-1):
    # Find the leftmost edge
    # Get the number to match on the tile above this one

    find = t_dict[id_grid[i-1][0]][1][0]
    for k, v in t_dict.items():
        if k in placed:
            continue
            
        if v[0][0] == find:
            pass
            # do nothing

        elif v[0][1] == find:
            # vertical
            flip_id_v(k)

        elif v[1][0] == find:
            # horizontal
            flip_id_h(k)

        elif v[1][1] == find:
            # clockwise * 2
            for j in range(2):
                rotate_id(k)

        elif v[2][0] == find:
            # clockwise, vertical
            for j in range(3):
                rotate_id(k)

            flip_id_v(k)

        elif v[2][1] == find:
            # clockwise
            for j in range(3):
                rotate_id(k)

        elif v[3][0] == find:
            # counter clock
            rotate_id(k)

        elif v[3][1] == find:
            # coutner clock, vertical
            rotate_id(k)

            flip_id_v(k)

        else:
            continue

        placed.add(k)
        grid[i][0] = t_dict2[k][:][:]
        id_grid[i][0] = k
        find = t_dict[k][3][0]

        break

    # Find the rest of the tiles in the grid
    for a in range(1, side):
        for k, v in t_dict.items():
            if k in placed:
                continue
                
            if v[0][0] == find:
                # counterclockwise, horizontal flip
                rotate_id(k)

                flip_id_h(k)

            elif v[0][1] == find:
                # counterclockwise
                rotate_id(k)

            elif v[1][0] == find:
                # clockwise
                for j in range(3):
                    rotate_id(k)

            elif v[1][1] == find:
                # clockwise, horizontal flip
                for j in range(3):
                    rotate_id(k)
                flip_id_h(k)

            elif v[2][0] == find:
                # Do nothing
                pass

            elif v[2][1] == find:
                # horizontal
                flip_id_h(k)

            elif v[3][0] == find:
                # vertical
                flip_id_v(k)

            elif v[3][1] == find:
                # clockwise * 2
                for j in range(2):
                    rotate_id(k)

            else:
                continue

            placed.add(k)
            grid[i][a] = t_dict2[k][:][:]
            id_grid[i][a] = k
            find = t_dict[k][3][0]

            break

# Fill in the final row, including the corners

# Find the lower left corner
find = t_dict[id_grid[side-2][0]][1][0]
for i in range(len(corners)):
    k = corners[i]
    v = t_dict[corners[i]]

    if k in placed:
        continue
        
    if v[0][0] == find:
        pass
        # do nothing

    elif v[0][1] == find:
        # vertical
        flip_id_v(k)

    elif v[1][0] == find:
        # horizontal
        flip_id_h(k)

    elif v[1][1] == find:
        # clockwise * 2
        for j in range(2):
            rotate_id(k)

    elif v[2][0] == find:
        # clockwise, vertical
        for j in range(3):
            rotate_id(k)

        flip_id_v(k)

    elif v[2][1] == find:
        # clockwise
        for j in range(3):
            rotate_id(k)

    elif v[3][0] == find:
        # counter clock
        rotate_id(k)

    elif v[3][1] == find:
        # coutner clock, vertical
        rotate_id(k)

        flip_id_v(k)

    else:
        continue

    corners.pop(i)
    placed.add(k)
    grid[side - 1][0] = t_dict2[k][:][:]
    id_grid[side-1][0] = k
    find = t_dict[k][3][0]

    break

# Find the lower edges
find = t_dict[id_grid[side-1][0]][3][0]
for i in range(1, side - 1):
    for k, v in t_dict.items():
        if k in placed:
            continue
            
        if v[0][0] == find:
            # counterclockwise, horizontal flip
            rotate_id(k)

            flip_id_h(k)

        elif v[0][1] == find:
            # counterclockwise
            rotate_id(k)

        elif v[1][0] == find:
            # clockwise
            for j in range(3):
                rotate_id(k)

        elif v[1][1] == find:
            # clockwise, horizontal flip
            for j in range(3):
                rotate_id(k)
            flip_id_h(k)

        elif v[2][0] == find:
            # Do nothing
            pass

        elif v[2][1] == find:
            # horizontal
            flip_id_h(k)

        elif v[3][0] == find:
            # vertical
            flip_id_v(k)

        elif v[3][1] == find:
            # clockwise * 2
            for j in range(2):
                rotate_id(k)

        else:
            continue

        placed.add(k)
        grid[side-1][i] = t_dict2[k][:][:]
        id_grid[side-1][i] = k
        find = t_dict[k][3][0]

        break

# Find the lower right corner (we know what it is, just have to orient it)
k = corners[0]
v = t_dict[corners[0]]

if v[0][0] == find:
    # counterclockwise, horizontal flip
    rotate_id(k)

    flip_id_h(k)

elif v[0][1] == find:
    # counterclockwise
    rotate_id(k)

elif v[1][0] == find:
    # clockwise
    for j in range(3):
        rotate_id(k)

elif v[1][1] == find:
    # clockwise, horizontal flip
    for j in range(3):
        rotate_id(k)
    flip_id_h(k)

elif v[2][0] == find:
    # Do nothing
    pass

elif v[2][1] == find:
    # horizontal
    flip_id_h(k)

elif v[3][0] == find:
    # vertical
    flip_id_v(k)

elif v[3][1] == find:
    # clockwise * 2
    for j in range(2):
        rotate_id(k)

placed.add(k)
grid[side-1][side - 1] = t_dict2[k][:][:]
id_grid[side - 1][side - 1] = k

######################
# After the worst code I've ever written in my entire life, all the tiles are oriented
# And placed correctly
#####################

for i in range(len(grid)):
    for j in range(len(grid)):
        grid[i][j] = remove_border(grid[i][j])

new_grid = []

for i in range(side):
    for j in range(8):
        line = [tile[j] for tile in grid[i]]
        new_grid.append(''.join(line))

########
# Now we have the final image, generate all orientations of it
########

images = []
images.append(new_grid)
images.append(rotate(new_grid))
images.append(rotate(rotate(new_grid)))
images.append(rotate(rotate(rotate(new_grid))))
images.append(flip_vertical(new_grid))
images.append(flip_horizontal(new_grid))
images.append(rotate(flip_vertical(new_grid)))
images.append(rotate(flip_horizontal(new_grid)))

for k, image in enumerate(images):
    for i, line in enumerate(image):
        image[i] = list(line)

    monsters = 0
    for i in range(len(image) - 2):
        for j in range(len(image[0]) - 19):
            if image[i][j+18] == '1' and image[i + 1][j] == '1' and image[i+1][j+5] == '1' and image[i+1][j+6] == '1' and image[i+1][j + 11] == '1' and image[i + 1][j + 12] == '1' and image[i+1][j+17] == '1' and image[i+1][j+18] == '1' and image[i+1][j+19] == '1' and image[i+2][j+1] == '1' and image[i+2][j+4] == '1' and image[i+2][j+7] == '1' and image[i+2][j+10] == '1' and image[i+2][j+13] == '1' and image[i+2][j+16] == '1':
                monsters += 1
                image[i][j+18] = '0'
                image[i + 1][j] = '0'
                image[i+1][j+5] = '0'
                image[i+1][j+6] = '0'
                image[i+1][j + 11] = '0'
                image[i + 1][j + 12] = '0'
                image[i+1][j+17] = '0'
                image[i+1][j+18] = '0'
                image[i+1][j+19] = '0'
                image[i+2][j+1] = '0'
                image[i+2][j+4] = '0'
                image[i+2][j+7] = '0'
                image[i+2][j+10] = '0'
                image[i+2][j+13] = '0'
                image[i+2][j+16] = '0'

    if monsters > 0:
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    ans += 1

print('Part 2:', ans)
