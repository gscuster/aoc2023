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

node = 'AAA'
index = 0
max_index = len(dir_data)
steps = 0

while node != 'ZZZ':
    next = direction[dir_data[index]]
    node = m[node][next]
    steps += 1
    index += 1
    if index >= max_index:
        index = 0

print(steps)
