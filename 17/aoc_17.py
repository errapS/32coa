import numpy as np
import heapq


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


def cheapest_path(grid, src, end, part1):
    priority_queue = [(0, -1, 0, src)]
    visited = {}
    paths = {vertex: [] for vertex in np.ndindex(grid.shape)}

    while priority_queue:
        current_distance, current_consecutive_steps, current_direction, current_vertex = heapq.heappop(priority_queue)

        if (current_consecutive_steps, current_direction, current_vertex) in visited:
            continue

        visited[(current_consecutive_steps, current_direction, current_vertex)] = current_distance

        for i, direction in enumerate([UP, RIGHT, DOWN, LEFT]):
            new_vertex = current_vertex[0] + direction[0], current_vertex[1] + direction[1]
            new_consecutive_steps = (1 if i != current_direction else current_consecutive_steps + 1)
            new_direction = i
            if part1:
                if 0 <= new_vertex[0] < rows and 0 <= new_vertex[1] < cols and new_consecutive_steps < 4 and (new_direction + 2) % 4 != current_direction:
                    weight = grid[new_vertex]
                    distance = current_distance + weight
                    paths[new_vertex] = paths[current_vertex] + [current_vertex]
                    heapq.heappush(priority_queue, (distance, new_consecutive_steps, new_direction, new_vertex))
            else:
                if 0 <= new_vertex[0] < rows and 0 <= new_vertex[1] < cols and (new_consecutive_steps < 11 and (current_consecutive_steps == -1 or current_consecutive_steps >= 4 or i == current_direction )) and (new_direction + 2) % 4 != current_direction:
                    weight = grid[new_vertex]
                    distance = current_distance + weight
                    paths[new_vertex] = paths[current_vertex] + [current_vertex]
                    heapq.heappush(priority_queue, (distance, new_consecutive_steps, new_direction, new_vertex))

    shortest_path_distance = []
    for (current_consecutive_steps, current_direction, current_vertex), dist in visited.items():
        if current_vertex == end:
            shortest_path_distance.append(dist)

    return min(shortest_path_distance) if shortest_path_distance else 0


city = np.array([list(map(int, line.strip())) for line in open('17/input.txt').read().split('\n')])

rows, cols = city.shape
start = (0, 0)
end = (rows - 1, cols - 1)

print('ANSWER PART A: ', cheapest_path(city, start, end, True))

print('ANSWER PART B: ', cheapest_path(city, start, end, False))