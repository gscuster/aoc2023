import numpy as np

def subtract_arr(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

f = open('input.txt', 'r')
d = f.readlines()
f.close()

galaxies = []
for i, line in enumerate(d):
    for j, value in enumerate(line):
        if value == '#':
            galaxies.append([i, j])

galaxy_row = [x[0] for x in galaxies]
galaxy_col = [x[1] for x in galaxies]

# Adjust modifier for part 1
modifier = 999999

## Adjust for empty rows
for i in reversed(range(len(d))):
    if i not in galaxy_row:
        for galaxy in galaxies:
            if galaxy[0] > i:
                galaxy[0] += modifier

## Adjust for empty columns
for i in reversed(range(len(d[0]))):
    if i not in galaxy_col:
        for galaxy in galaxies:
            if galaxy[1] > i:
                galaxy[1] += modifier

distance = []
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        distance.append(subtract_arr(galaxies[i], galaxies[j]))

print(sum(distance))