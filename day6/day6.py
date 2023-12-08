import math

# d = t*(r-t) = rt - t^2
# 0 = -t^2 + rt - d
# 0 = ax^2 + bt + c
def race_poly_roots(d, r):
    b24ac = math.sqrt(math.pow(r, 2) - 4 * d)
    root1 = (-r + b24ac)/ -2
    root2 = (-r - b24ac)/ -2
    return (math.ceil(root1), math.ceil(root2))

f = open('input.txt', 'r')
d = f.readlines()
f.close()

times = [int(x) for x in d[0].split()[1:]]
distances = [int(x) for x in d[1].split()[1:]]

values = []
for i in range(len(times)):
    roots = race_poly_roots(distances[i], times[i])
    values.append(roots[1] - roots[0])

result = 1
for value in values:
    result *= value

print(result)