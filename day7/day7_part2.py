m = {'2': '02',
     '3': '03',
     '4': '04',
     '5': '05',
     '6': '06',
     '7': '07',
     '8': '08',
     '9': '09',
     'T': '10',
     'J': '00',
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
    vals_wo_jack = [char_count[i] for i in char_count.keys() if i != 'J']

    if len(vals_wo_jack) > 0:
        max_wo_jack = max(vals_wo_jack)
    else:
        max_wo_jack = 0

    if 'J' in char_count:
        j_count = char_count['J']
    else:
        j_count = 0

    if 5 in vals or (max_wo_jack + j_count) == 5:
        result = '7'
    elif 4 in vals or (max_wo_jack + j_count) == 4:
        result = '6'
    elif 3 in vals and 2 in vals:
        result = '5'
    elif list(vals).count(2) == 2 and j_count:
        result = '5'
    elif 3 in vals or (max_wo_jack + j_count) == 3:
        result = '4'
    elif 2 in vals or (max_wo_jack + j_count) == 2:
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
