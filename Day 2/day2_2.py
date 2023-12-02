from functools import reduce
total = 0 

def process_row(row):
    game_id, game_results = row.split(':')
    game_id = int(game_id.replace('Game ', ''))
    draws = game_results.split(';')
    draw_maximums = dict()
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            _,count,color = cube.split(' ')
            if draw_maximums.get(color, 0) < int(count):
                draw_maximums[color] = int(count)
    return reduce(lambda x, y: x*y, draw_maximums.values())


with open('inputs/day2.txt') as f:
    for line in f:
        total += process_row(line.strip())
print(total)
