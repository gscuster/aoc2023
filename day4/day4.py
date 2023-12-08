import math
def calculate_points(line):
    [winners, values] = [x.split() for x in line.split('|')]
    winners_you_have = [x for x in values if x in winners]
    if len(winners_you_have) > 0:
        return 2**(len(winners_you_have) - 1)
    else:
        return 0
    
def winning_values(line):
    [winners, values] = [x.split() for x in line.split('|')]
    return [x for x in values if x in winners]


f = open('input.txt', 'r')
d = f.readlines()
f.close()

points = []
for line in d:
    points.append(calculate_points(line))

print(sum(points))

def update_count(count, idx, line):
    winning_count = len(winning_values(line))
    for i in range(idx+1,idx + winning_count + 1):
        count[i] += count[idx]

card_count = [1]*len(d)
for i, line in enumerate(d):
   update_count(card_count, i, line)

print(sum(card_count))