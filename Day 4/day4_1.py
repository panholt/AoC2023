import re 

scratch_card_re = re.compile(r'^Card\s+(\d+):(.*?)\|(.*)$')

def prepare_data():
    output = dict()
    with open('inputs/day4.txt') as f:
        for line in f:
            m = scratch_card_re.search(line)
            if m:
                card_number = m.group(1)
                output[card_number] = dict()
                output[card_number]['winning_numbers'] = [num for num in m.group(2).split() if num.isdigit()]
                output[card_number]['card_numbers'] = [num for num in m.group(3).split() if num.isdigit()]
            else:
                print('Bad regex')
    return output

data = prepare_data()
total = 0
for card_number, card_data in data.items():
    winning_numbers = [num for num in card_data['card_numbers'] if num in card_data['winning_numbers']]
    count_of_winning_numbers = len(winning_numbers)
    if count_of_winning_numbers == 0:
        continue
    if count_of_winning_numbers == 1:
        total += 1
    else:
        exponent =  pow(2, count_of_winning_numbers - 1)
        total += exponent
print(total)