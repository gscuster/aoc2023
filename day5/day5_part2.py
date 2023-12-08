f = open('test_input.txt', 'r')
d = f.read()
f.close()

def parse_map(data):
    lines = data.splitlines()
    unordered_result = [list(map(int, x.split())) for x in lines[1:]]
    modified = [[x[0] - x[1], x[1], x[1] + x[2]] for x in unordered_result]
    return modified

def match(value, arr):
    if arr[1] <= value < arr[2]:
        return value + arr[0]

def find_match(value, m, start_idx, idx):
    result = match(value, m[start_idx[idx]])
    if not result:
        for i, arr in enumerate(m):
            if i == start_idx[idx]:
                continue
            result = match(value, arr)
            if result:
                start_idx[idx] = i
                break
    if not result:
        result = value
    return result

categories = d.split('\n\n')

seeds_raw = [int(x) for x in categories[0].split()[1:]]

seed_ranges = [[seeds_raw[i], seeds_raw[i] + seeds_raw[i+1]] for i in range(0, len(seeds_raw), 2)]

map_data = [parse_map(x) for x in categories[1:]]

min_loc = 10000000000000
n = 0
start_idx = [0]*len(map_data)
for seed_range in seed_ranges:
    for seed in range(seed_range[0], seed_range[1]):
        if n%1000000 == 0:
            print("On cycle ", n)
        s = find_match(seed, map_data[0], start_idx, 0)
        f = find_match(s, map_data[1], start_idx, 1)
        w = find_match(f, map_data[2], start_idx, 2)
        l = find_match(w, map_data[3], start_idx, 3)
        t = find_match(l, map_data[4], start_idx, 4)
        h = find_match(t, map_data[5], start_idx, 5)
        loc = find_match(h, map_data[6], start_idx, 6)
        if loc < min_loc:
            min_loc = loc
        n+=1

print(min_loc)
# 60294664