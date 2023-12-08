import re
import numpy as np

def symbol_value(line):
    x = []
    for c in line:
        if re.match(r'[^*]', c):
            x.append(0)
        else:
            x.append(1)
    return x

f = open('input.txt', 'r')
d = f.read().splitlines()
f.close()

line_length = len(d[0])

filler = '.'*line_length

filled = [filler] + d + [filler]

symbol_data = np.array(list(map(symbol_value, filled)))

part_map = {}
for i in range(1, len(filled)):
    values = re.findall(r'\d+|[^\d]',filled[i])
    start = 0
    for value in values:
        end = start + len(value)

        if start == 0:
            check_start = 0
        else:
            check_start = start - 1

        if end >= line_length:
            check_end = line_length-1
        else:
            check_end = end + 1

        if value.isnumeric():
            for j in range(i-1,i+2):
                for k in range(check_start,check_end):
                    if symbol_data[j][k]:
                        position = k + j * line_length
                        if position in part_map:
                            part_map[position].append(value)
                        else:
                            part_map[position] = [value]
        start += len(value)

gears = []
for key in part_map:
    if len(part_map[key]) == 2:
        gears.append(int(part_map[key][0])*int(part_map[key][1]))

print(sum(gears))