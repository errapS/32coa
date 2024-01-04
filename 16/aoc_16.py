import numpy as np


def tiles(grid, beam_position, beam_direction):
    rows, cols = grid.shape

    while 0 <= beam_position[0] < rows and 0 <= beam_position[1] < cols:
        current_tile = grid[beam_position]

        if (beam_position, beam_direction) not in visited_tiles:
            visited_tiles.add((beam_position, beam_direction))
        else:
            return

        if current_tile == '\\':
            beam_direction = (beam_direction[1], beam_direction[0])
        elif current_tile == '/':
            beam_direction = (-beam_direction[1], -beam_direction[0]) 

        elif current_tile == '|' and beam_direction[0] == 0:
            tiles(layout, (beam_position[0]-1, beam_position[1]), (-1, 0))  
            tiles(layout, (beam_position[0]+1, beam_position[1]), (1, 0))
            return
        
        elif current_tile == '-' and beam_direction[1] == 0:
            tiles(layout, (beam_position[0], beam_position[1]+1), (0, 1))
            tiles(layout, (beam_position[0], beam_position[1]-1), (0, -1))
            return
        
        beam_position = (beam_position[0] + beam_direction[0], beam_position[1] + beam_direction[1])

    dead_ends.add(((beam_position[0] - beam_direction[0], beam_position[1] - beam_direction[1]), flip_mapping[beam_direction]))
    return 


layout = np.array([list(line) for line in open('16/input.txt').read().split('\n')])
visited_tiles = set()
dead_ends = set()
flip_mapping = {(1, 0): (-1, 0), (-1, 0): (1, 0), (0, 1): (0, -1), (0, -1): (0, 1)}

tiles(layout, (0, 0), (0, 1))

r = set()
for c, d in visited_tiles:
    r.add(c)

print('ANSWER PART A', len(r))


dead_ends = set()
beam_sp = []
rows, cols = layout.shape

for r in range(rows):
    beam_sp.extend((((r,cols-1), (0, -1)), ((r, 0), (0, 1))))
for c in range(cols):
    beam_sp.extend((((rows-1, c), (-1, 0)), ((0, c), (1, 0))))

max_tiles = 0
for start in beam_sp:
    visited_tiles = set()
    if start in dead_ends:
        continue
    
    tiles(layout, start[0], start[1])

    r = set()
    for c, d in visited_tiles:
        r.add(c)

    if len(r) > max_tiles:
        max_tiles = len(r)

print('ANSWER PART B', max_tiles)
