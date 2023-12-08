import re
import numpy as np

def symbol_value(line):
    x = []
    for c in line:
        if re.match(r'[\d\.]', c):
            x.append(0)
        else:
            x.append(1)
    return x

f = open('input.txt', 'r')
d = f.read().splitlines()
f.close()

filler = '.'*len(d[0])

filled = [filler] + d + [filler]

symbol_data = np.array(list(map(symbol_value, filled)))

part_number = []
for i in range(1, len(filled)):
    symbol_count = np.sum(symbol_data[i-1:i+2],0)
    values = re.findall(r'\d+|[^\d]',filled[i])
    start = 0
    for value in values:
        end = start + len(value)

        if start == 0:
            check_start = 0
        else:
            check_start = start - 1

        if end == len(filled)-1:
            check_end = len(filled)-1
        else:
            check_end = end + 1

        if value.isnumeric() and np.sum(symbol_count[check_start:check_end]) > 0:
            part_number.append(int(value))
        start += len(value)

print(sum(part_number))