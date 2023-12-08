m = {'2': '02',
     '3': '03',
     '4': '04',
     '5': '05',
     '6': '06',
     '7': '07',
     '8': '08',
     '9': '09',
     'T': '10',
     'J': '11',
     'Q': '12',
     'K': '13',
     'A': '14'}

def hand_value(s):
    char_count = {}
    postfix = ''
    for char in s:
        postfix += m[char]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    vals = char_count.values()
    if 5 in vals:
        result = '7'
    elif 4 in vals:
        result = '6'
    elif 3 in vals and 2 in vals:
        result = '5'
    elif 3 in vals:
        result = '4'
    elif 2 in vals:
        if list(vals).count(2) == 2:
            result = '3'
        else:
            result = '2'
    else:
        result = '1'
    return int(result + postfix)

f = open('input.txt', 'r')
d = f.readlines()
f.close()

hands = []
for line in d:
    data = line.split()
    hands.append([data[0], int(data[1]), hand_value(data[0])])

sorted_hands = sorted(hands, key=lambda x: x[2], reverse=True)

total = 0
rank = len(sorted_hands)
for hand in sorted_hands:
    total += hand[1] * rank
    hand.append(rank)
    rank -= 1

print(total)
print(sorted_hands)
