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

time = int("".join(d[0].split()[1:]))
distance = int("".join(d[1].split()[1:]))

roots = race_poly_roots(distance, time)

print(roots[1] - roots[0])