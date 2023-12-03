import re

def prepare_data():
    ret = dict()
    with open('inputs/day3.txt') as f:
        for row,data in enumerate(f, 1):
            ret[row] = data.strip()
    return ret

def count_of_adjacent_symbols(slice):
    return len(re.findall(r'[^\w\.]', slice))

def num_adjacences(match, row_idx):
    start,stop = match.span()
    start = max(start - 1, 0)
    count_of_prior_row_slice = count_of_adjacent_symbols(data.get(row_idx - 1, '')[start:stop+1])
    count_of_current_row_slice = count_of_adjacent_symbols(data[row_idx][start:stop+1])
    count_of_next_row_slice = count_of_adjacent_symbols(data.get(row_idx + 1, '')[start:stop+1])
    return count_of_next_row_slice + count_of_current_row_slice + count_of_prior_row_slice

def process_row(row_idx, row_data):
    hits = []
    matches = re.finditer('(\d+)', row_data)
    for match in matches:
        num = num_adjacences(match, row_idx)
        for _ in range(num):
            hits.append(int(match.group(1)))
    return hits

hits = []
data = prepare_data()
for row,row_data in data.items():
    hits.extend(process_row(row, row_data))
print(sum(hits))