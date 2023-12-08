import re
import string

number_map = {'one': '1',
              'two': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9'}

def string_to_number (s):
    if not s.isnumeric():
        return number_map[s]
    else:
        return s

f = open('input.txt', 'r')
d = f.readlines()
f.close()

match_exp = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

all_numbers = [re.findall(match_exp,i) for i in d]

numbers = [int(string_to_number(x[0]) + string_to_number(x[-1])) for x in all_numbers]

total = sum(numbers)