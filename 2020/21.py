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

    with open('21-test.txt', 'w') as f:
        f.write(raw)
        f.write('\n')

elif args.repeat_test:
    raw = open('21-test.txt', 'r').read().strip()

else:
    raw = open('21-input.txt', 'r').read().strip()

lines = raw.split('\n')

try:
    nums = [int(line) for line in lines]
except Exception as e:
    pass

# Part 1
ans = 0

d = {}
alergen_set = set()
ingredient_set = set()
ingredient_counts = {}

for line in lines:
    paren_idx = line.index('(')
    contain_idx = line.index('contains')

    ingredients = line[:paren_idx-1].split(' ')
    alergens = line[contain_idx + 9:-1].split(', ')

    for alergen in alergens:
        alergen_set.add(alergen)

    for ingredient in ingredients:
        ingredient_set.add(ingredient)

        if ingredient in ingredient_counts:
            ingredient_counts[ingredient] += 1
        else:
            ingredient_counts[ingredient] = 1

    for ingredient in ingredients:
        if ingredient not in d:
            d[ingredient] = {alergen: 1 for alergen in alergens}
        else:
            for alergen in alergens:
                if alergen not in d[ingredient]:
                    d[ingredient][alergen] = 1
                else:
                    d[ingredient][alergen] += 1

found_alergens = set()
alergen_foods = set()
alergen_ingredient = {}

while len(found_alergens) != len(alergen_set):
    for alergen in alergen_set:
        if alergen in found_alergens:
            continue

        valid = False
        max_count = -1
        max_ingredient = ''
        for ingredient, alergen_counts in d.items():
            if alergen in alergen_counts and alergen_counts[alergen] > max_count:
                max_count = alergen_counts[alergen]
                max_ingredient = ingredient
                valid = True
            elif alergen in alergen_counts and alergen_counts[alergen] == max_count:
                valid = False

        if valid and max_count > -1:
            alergen_ingredient[alergen] = max_ingredient
            found_alergens.add(alergen)
            alergen_foods.add(max_ingredient)
            del d[max_ingredient]

            for i, a in d.items():
                if alergen in a:
                    del a[alergen]

            break

non_alergens = ingredient_set - alergen_foods

for ingredient in non_alergens:
    ans += ingredient_counts[ingredient]

print('Part 1:', ans)

###########################

# Part 2
ans = 0

a = [b for b in alergen_ingredient.items()]
a.sort()

ans = ','.join([b[1] for b in a])

print('Part 2:', ans)
