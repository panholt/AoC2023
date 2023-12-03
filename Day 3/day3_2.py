import re

def prepare_data():
    ret = dict()
    with open('inputs/day3.txt') as f:
        for row,data in enumerate(f, 1):
            ret[row] = data.strip()
    return ret

def count_of_adjacent_symbols(slice):
    return len(re.findall(r'[^\w\.]', slice))

def find_adjacent_numbers(row_idx, position):
    results = []
    # Previous Row
    for m in re.finditer('(\d+)', data.get(row_idx - 1, '')):
        start,stop = m.span()
        start = max(start - 1, 0)
        stop = min(140, stop + 1)
        if position in range(start,stop):
            results.append(int(m.group(1)))
    #Current Row
    for m in re.finditer('(\d+)', data.get(row_idx, '')):
        start,stop = m.span()
        start = max(start - 1, 0)
        stop = min(140, stop + 1)
        if position in range(start,stop):
            results.append(int(m.group(1)))
    for m in re.finditer('(\d+)', data.get(row_idx + 1, '')):
        start,stop = m.span()
        start = max(start - 1, 0)
        stop = min(140, stop + 1)
        if position in range(start,stop):
            results.append(int(m.group(1)))
    return results

def process_row(row_idx, row_data):
    hits = []
    matches = re.finditer('\*', row_data)
    for match in matches:
        adjacent_numbers = find_adjacent_numbers(row_idx, match.span()[0])
        if len(adjacent_numbers) == 2:
            hits.append(adjacent_numbers[0] * adjacent_numbers[1])
    return hits

hits = []
data = prepare_data()
for row,row_data in data.items():
    hits.extend(process_row(row, row_data))
print(sum(hits))