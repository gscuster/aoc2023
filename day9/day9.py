import numpy as np

f = open('input.txt', 'r')
d = f.readlines()
f.close()

def next_val(arr):
    diff = [arr, np.ediff1d(arr)]
    while np.any(diff[-1]):
        diff.append(np.ediff1d(diff[-1]))
    for i in reversed(range(1,len(diff))):
        diff[i-1] = np.append(diff[i-1], diff[i-1][-1] + diff[i][-1])
    return diff[0][-1]

# Add to end
total = 0
for line in d:
    linedata = np.array([int(x) for x in line.split()])
    total += next_val(linedata)

print(total)

# Add to beginning (just flip the sequence)
total = 0
for line in d:
    linedata = np.flip(np.array([int(x) for x in line.split()]))
    total += next_val(linedata)

print(total)