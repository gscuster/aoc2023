import re
f = open('input.txt', 'r')
d = f.readlines()
f.close()

direction = {'L': 0, 'R': 1}
dir_data = d[0].strip()

m = {}
for line in d[2:]:
    linedata = re.findall(r'\w{3}', line)
    m[linedata[0]] = [linedata[1], linedata[2]]

nodes = [x for x in m.keys() if x[-1] == 'A']
origin = nodes.copy()
first_z = [0]*n
n = len(nodes)
cycle_len = [0]*n
max_index = len(dir_data)

seen = []
for node in nodes:
    seen.append([[], [], [0]])

steps = 0
index = 0
while 0 in cycle_len:
    if steps % 1000000 == 0:
        print("On step: ", steps)
        print(seen)
    next = direction[dir_data[index]]
    steps += 1
    index += 1
    if index >= max_index:
        index = 0
    for i in range(n):
        nodes[i] = m[nodes[i]][next]
        if cycle_len[i] == 0:
            if nodes[i][-1] == 'Z':
                seen[i][0].append(nodes[i])
                seen[i][1].append(steps - seen[i][2][-1])
                seen[i][2].append(steps)
            if len(seen[i][1]) > 5 and all(x == seen[i][1][-5] for x in seen[i][1][-4:]):
                cycle_len[i] = seen[i][1][-1]
print(cycle_len)

def first_z(seen, cycle):
    seq = (x for x in seen[cycle[0]:] if x[-1] == 'Z')
    return seen.index(next(seq))