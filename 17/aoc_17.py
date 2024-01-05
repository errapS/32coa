import numpy as np
import heapq


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

def is_valid(node, consecutive_steps, direction, previous_direction):
    if consecutive_steps == 3 and direction == previous_direction:
        return False
    elif 0 <= node[0] < rows and 0 <= node[1] < cols:
        return True
    return False
    

def cheapest_path(grid, src, end):
    priority_queue = [(grid[src], 1, 0, src)]
    visited = set()

    distances = {vertex: float('infinity') for vertex in np.ndindex(grid.shape)}
    distances[src] = grid[src]
    consecutive_steps_count = {vertex: 1 for vertex in np.ndindex(grid.shape)}

    while priority_queue:
        current_distance, current_consecutive_steps, previous_direction, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor in [UP, RIGHT, DOWN, LEFT]:
            dx, dy = neighbor
            new_vertex = current_vertex[0] + dx, current_vertex[1] + dy
            
            if is_valid(new_vertex, current_consecutive_steps, neighbor, previous_direction):
                weight = grid[new_vertex]
                distance = current_distance + weight

                if distance < distances[new_vertex]:
                    distances[new_vertex] = distance

                    if neighbor == previous_direction or previous_direction == 0:
                        consecutive_steps_count[new_vertex] = current_consecutive_steps + 1

                    heapq.heappush(priority_queue, (distance, consecutive_steps_count[new_vertex], neighbor, new_vertex))
                   
    shortest_path_distance = distances[end]
    
    return shortest_path_distance



city = np.array([list(map(int, line.strip())) for line in open('17/test.txt').read().split('\n')])

rows, cols = city.shape
start = (0, 0)
end = (rows - 1, cols - 1)

r =cheapest_path(city, start, end)
print(r)