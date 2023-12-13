def difference(s1, s2, limit):
    difference = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            difference += 1
            if difference > limit:
                break
    return difference

def check_row_pattern_diff(p):
    result = 0
    for i in range(1, len(p)):
        diff = difference(p[i], p[i-1], 1)
        if diff <= 1:
            n = min(len(p) - i, i)
            reflected = True
            for j in range(1, n):
                diff += difference(p[i + j], p[i - j - 1], 1-diff)
                if diff > 1:
                    reflected = False
                    break
            if reflected and diff == 1:
                result = i
                break
    return result

def check_row_pattern(p):
    result = 0
    for i in range(1, len(p)):
        if p[i] == p[i-1]:
            n = min(len(p) - i, i)
            reflected = True
            for j in range(1, n):
                if p[i + j] != p[i - j - 1]:
                    reflected = False
                    break
            if reflected:
                result = i
                break
    return result

def pattern_reflection(p):
    # Check rows first
    result = check_row_pattern(p)*100
    d_result = check_row_pattern_diff(p)*100
    tp = [''.join(s) for s in zip(*p)]
    if not result:
        result = check_row_pattern(tp)
    if not d_result:
        d_result = check_row_pattern_diff(tp)
    return (result, d_result)

f = open('input.txt', 'r')
d = f.readlines()
f.close()

patterns = []
pattern = []
for line in d:
    if line.strip() == '':
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(line.strip())
patterns.append(pattern)

total = 0
total_d = 0
for pattern in patterns:
    (result, d_result) = pattern_reflection(pattern)
    total += result
    total_d += d_result

print(total)
print(total_d)