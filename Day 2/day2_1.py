limits = {'red': 12, 'green': 13, 'blue': 14} 
total = 0 

def process_row(row):
    game_id, game_results = row.split(':')
    game_id = int(game_id.replace('Game ', ''))
    draws = game_results.split(';')
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            _,count,color = cube.split(' ')
            if int(count) > limits.get(color):
                return 0
    return game_id


with open('inputs/day2.txt') as f:
    for line in f:
        total += process_row(line.strip())
print(total)
