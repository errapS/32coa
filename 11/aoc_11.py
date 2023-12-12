import numpy as np

image = np.array([list(line.strip()) for line in open('11/input.txt').readlines()])

dots = image == '.'
delta_rows = np.cumsum(np.all(dots, axis=1).astype(int))
delta_cols = np.cumsum(np.all(dots, axis=0).astype(int))

rows = np.arange(len(delta_rows)) + delta_rows
cols = np.arange(len(delta_cols)) + delta_cols

galaxies = np.where(image == '#')

expanded_rows = galaxies[0]
for i in range(len(expanded_rows)):
    expanded_rows[i] += delta_rows[expanded_rows[i]]

expanded_cols = galaxies[1]
for i in range(len(expanded_cols)):
    expanded_cols[i] += delta_cols[expanded_cols[i]]

coordinates = np.column_stack((expanded_cols, expanded_rows))

# pairwise manhattan distances
distances = np.abs(coordinates[:, np.newaxis, 0] - coordinates[:, 0]) + np.abs(coordinates[:, np.newaxis, 1] - coordinates[:, 1])

matrix_sum = np.sum(distances)//2

print('ANSWER PART A: ', matrix_sum)



expansion = 1_000_000
delta_rows = np.cumsum(np.all(dots, axis=1).astype(int) * (expansion-1))
delta_cols = np.cumsum(np.all(dots, axis=0).astype(int) * (expansion-1))

rows = np.arange(len(delta_rows)) + delta_rows
cols = np.arange(len(delta_cols)) + delta_cols

galaxies = np.where(image == '#')

expanded_rows = galaxies[0]
for i in range(len(expanded_rows)):
    expanded_rows[i] += delta_rows[expanded_rows[i]]

expanded_cols = galaxies[1]
for i in range(len(expanded_cols)):
    expanded_cols[i] += delta_cols[expanded_cols[i]]

coordinates = np.column_stack((expanded_cols, expanded_rows))

# pairwise manhattan distances
distances = np.abs(coordinates[:, np.newaxis, 0] - coordinates[:, 0]) + np.abs(coordinates[:, np.newaxis, 1] - coordinates[:, 1])

matrix_sum = np.sum(distances)//2

print('ANSWER PART B: ', matrix_sum)