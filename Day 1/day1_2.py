import re

total = 0
words = {'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'}

with open('inputs/day1.txt') as f:
    for line in f.readlines():
        digits = re.findall(f'(?=({"|".join(words.keys())}|\d))', line)
        first_digit = words.get(digits[0]) or digits[0]
        second_digit = words.get(digits[-1]) or digits[-1]
        calibration_value = int(first_digit + second_digit)
        total += calibration_value
print(total)