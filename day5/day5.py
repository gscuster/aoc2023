f = open('input.txt', 'r')
d = f.read()
f.close()

def parse_map(data):
    lines = data.splitlines()
    unordered_result = [list(map(int, x.split())) for x in lines[1:]]
    return sorted(unordered_result, key=lambda x: x[1])

def find_match(value, m):
    for arr in m:
        print(arr)
        if value >= arr[1] and value < arr[1] + arr[2]:
            return arr[0] + value - arr[1]
        elif value < arr[1]:
            return value
    return value

categories = d.split('\n\n')

seeds = [int(x) for x in categories[0].split()[1:]]

map_data = [parse_map(x) for x in categories[1:]]

min_loc = 10000000000000
seed_data = {}
for seed in seeds:
    s = find_match(seed, map_data[0])
    f = find_match(s, map_data[1])
    w = find_match(f, map_data[2])
    l = find_match(w, map_data[3])
    t = find_match(l, map_data[4])
    h = find_match(t, map_data[5])
    loc = find_match(h, map_data[6])
    if loc < min_loc:
        min_loc = loc
    seed_data[seed] = [s, f, w, l, t, h, loc]

print(min_loc)