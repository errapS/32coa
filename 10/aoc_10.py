import re

maze = open('10/input.txt').read().split('\n')

directions_map = {'|': {'N': 'N', 'S': 'S'},
                '-': {'W': 'W', 'E': 'E'},
                'L': {'W': 'N', 'S': 'E'},
                'J': {'E': 'N', 'S': 'W'},
                '7': {'E': 'S', 'N': 'W'}, 
                'F': {'W': 'S', 'N': 'E'}}

x_len = len(maze[0])
y_len = len(maze)

for i, line in enumerate(maze):
    s_str = re.search('S', line)
    if s_str != None:
        S = (s_str.start(), i)
        break


start_position = S
directions = {'W': (-1,0), 'E': (1,0), 'N': (0,-1), 'S': (0,1)}
path = []
for d in directions:
    direction = d
    position = tuple(map(lambda i, j: i + j, start_position, directions[direction]))
    steps = 0
    while True:
        pipe = maze[position[1]][position[0]]
        if pipe == '.':
            break
        elif pipe == 'S':
            steps += 1
            break
        elif direction in directions_map[pipe]:
            if len(path) == 0:
                path.append((start_position[1], start_position[0]))
            path.append((position[1], position[0]))
            direction = directions_map[pipe][direction]
            position = tuple(map(lambda i, j: i + j, position, directions[direction]))
            if 0 >= position[0] > x_len or 0 >= position[1] > y_len:
                break  
            steps += 1
        else:
            break
    if steps != 0:
        break

print('ANSWER A: ', steps//2)


def picks_theorem(path):
    B = len(path)
    S = 0
    for i in range(B):
        x1, y1 = path[i]
        x2, y2 = path[(i + 1) % B] 
        S += x1 * y2 - x2 * y1
    I = abs(S) // 2 - B // 2 + 1

    return I

points_inside = picks_theorem(path)
print('ANSWER B: ', points_inside)










