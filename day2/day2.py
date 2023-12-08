import re

m = {"red": 12,
     "green": 13,
     "blue": 14}

def possible_game(line):
    green_count = [int(x) for x in re.findall(r'\d+\s(?=green)', line)]
    if max(green_count) > 13:
        return False
    red_count = [int(x) for x in re.findall(r'\d+\s(?=red)', line)]
    if max(red_count) > 12:
        return False
    blue_count = [int(x) for x in re.findall(r'\d+\s(?=blue)', line)]
    if max(blue_count) > 14:
        return False
    return True

def game_power(line):
    green_count = [int(x) for x in re.findall(r'\d+\s(?=green)', line)]
    red_count = [int(x) for x in re.findall(r'\d+\s(?=red)', line)]
    blue_count = [int(x) for x in re.findall(r'\d+\s(?=blue)', line)]
    return max(green_count)*max(red_count)*max(blue_count)

f = open('input.txt', 'r')
d = f.readlines()
f.close()

possible = []

n = 1
for line in d:
    if possible_game(line):
        possible.append(n)
    n += 1

total = sum(possible)

print(total)

power = []
for line in d:
    power.append(game_power(line))

print(sum(power))