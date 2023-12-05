import re
from functools import reduce

config = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
for i, line in enumerate(open('02/input.txt').readlines()):
    matches = re.compile(r'(\d+)\s([a-zA-Z]+)').findall(line)
    game_values = [int(match[0]) for match in matches]
    max_game_values = [config[match[1]] for match in matches]
    
    if not [j + 1 for j, (num, cor) in enumerate(zip(game_values, max_game_values)) if num > cor]:
        sum += i + 1
   
print('ANSWER PART A: ', sum)

sum = 0
for i, line in enumerate(open('02/input2.txt').readlines()):
    matches = re.compile(r'(\d+)\s([a-zA-Z]+)').findall(line)
    game_values = [int(match[0]) for match in matches]
    colors = [match[1] for match in matches]

    val = {'red': 0, 'green': 0, 'blue': 0}
    val = {col: num if num > val[col] else val[col] for num, col in sorted(zip(game_values, colors))}
    sum += reduce(lambda x, y: x * y, val.values())

print('ANSWER PART B: ', sum)



