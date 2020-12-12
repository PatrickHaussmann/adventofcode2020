import numpy as np

with open('11/input.txt', 'r') as reader:
    lines = [[c for c in line.strip()] for line in reader if line.strip()]

grid = np.array(lines)
shape = grid.shape

Adjacents = {(-1, 1), (0, 1), (1, 1), (-1, 0),
             (1, 0), (-1, -1), (0, -1), (1, -1)}


def NumberOfNeighbors(r, c, g):
    neighbors = 0
    for dr, dc in Adjacents:
        if 0 <= r+dr < shape[0] and 0 <= c+dc < shape[1]:  # valid space on grid
            if grid[r+dr][c+dc] == "#":
                neighbors += 1

    return neighbors


while True:
    new_grid = np.copy(grid)

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            seat = grid[row][col]
            if seat == ".":
                continue

            neighbors = NumberOfNeighbors(row, col, grid)

            if seat == "L" and neighbors == 0:
                new_grid[row][col] = "#"

            if seat == "#" and neighbors >= 4:
                new_grid[row][col] = "L"

    if np.array_equal(grid, new_grid):
        break
    grid = new_grid
    # print(grid)


count = 0
for row in grid:
    for val in row:
        if val == "#":
            count += 1

print(count)
