def count_broken(s):
    count = 0
    result = []
    for char in s:
        if char == '#':
            count += 1
        elif count > 0:
            result.append(count)
            count = 0
    if count > 0:
        result.append(count)
    return result

def build_string(s, mask):
    result = ''
    q_count = 0
    for character in s:
        if character == '?':
            if 2**q_count & mask:
                result += '#'
            else:
                result += '.'
            q_count += 1
        else:
            result += character
    return result

f = open('input.txt', 'r')
d = f.readlines()
f.close()

total = 0
for line in d:
    [line_s, line_b] = line.split()
    line_broken = [int(x) for x in line_b.split(',')]
    line_q = line.count('?')
    line_possible = 0
    # Go through all permutations
    for i in range(2**line_q):
        s = build_string(line_s, i)
        if count_broken(s) == line_broken:
            line_possible += 1
    total += line_possible

print(total)