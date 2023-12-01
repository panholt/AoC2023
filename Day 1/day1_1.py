import re

total = 0

with open("inputs/day1.txt") as f:
    for line in f.readlines():
        digits = re.findall("\d", line)
        calibration_value = int(digits[0] + digits[-1])
        total += calibration_value
print(total)