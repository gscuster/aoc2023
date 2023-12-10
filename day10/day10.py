import numpy as np

f = open('input.txt', 'r')
d = f.readlines()
f.close()

#                           N        S       E       W
directions = np.array([[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]])

m = {'|': [0, 1, 2, 0, 0],
     '-': [0, 0, 0, 3, 4],
     'L': [0, 0, 3, 0, 1],
     'J': [0, 0, 4, 1, 0],
     '7': [0, 4, 0, 2, 0],
     'F': [0, 3, 0, 0, 2],
     '.': [0, 0, 0, 0, 0]}

data = []
start = []
for i, line in enumerate(d):
    data.append(line.strip())
    if 'S' in line:
        start = [i, line.index('S')]

print(start)
connections = []
direction = []
all_points = [np.array(start)]
# Check west
if m[data[start[0]][start[1] - 1]][3]:
    connections.append(np.array([start[0], start[1] - 1]))
    direction.append(4)
# Check east
if m[data[start[0]][start[1] + 1]][4]:
    connections.append(np.array([start[0], start[1] + 1]))
    direction.append(3)
# Check north
if m[data[start[0] - 1][start[1]]][2]:
    connections.append(np.array([start[0] - 1, start[1]]))
    direction.append(1)
# Check south
if m[data[start[0] + 1][start[1]]][1]:
    connections.append(np.array([start[0], start[1]]))
    direction.append(2)

all_points.extend(connections)

if len(connections) > 2:
    print("This won't work")
else:
    print(connections)

step = 1
while np.any(connections[0] != connections[1]):
    step += 1
    next_a = connections[0] + directions[direction[0]]
    next_b = connections[1] + directions[direction[1]]
    if np.all(next_a == connections[1]) or np.all(next_b == connections[0]):
        break
    connections[0] = next_a
    connections[1] = next_b
    all_points.extend(connections)
    direction[0] = m[data[connections[0][0]][connections[0][1]]][direction[0]]
    direction[1] = m[data[connections[1][0]][connections[1][1]]][direction[1]]

print(step)

side_char = {'|': [],
             'L': ['7'],
             'J': [],
             '7': [],
             'F': ['J']}

all_points_array = np.array(all_points)
all_points_list = [list(x) for x in all_points]
min_x_y = all_points_array.min(axis=0)
max_x_y = all_points_array.max(axis=0)

inside_count = 0
# i is the line index. j is the column index
for i in range(min_x_y[0], max_x_y[0] + 1):
    side_count = 0
    prev_side = '|'
    for j in range(min_x_y[1], max_x_y[1] + 1):
        if [i, j] in all_points_list:
            if data[i][j] in side_char.keys() and data[i][j] not in side_char[prev_side]:
                side_count += 1
                prev_side = data[i][j]
        elif side_count%2 == 1:
            inside_count += 1

print(inside_count)