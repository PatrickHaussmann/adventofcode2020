import numpy as np

with open('11/input.txt', 'r') as reader:
    lines = [[c for c in line.strip()] for line in reader if line.strip()]

grid = np.array(lines)
shape = grid.shape

Directions = {(-1, 1), (0, 1), (1, 1), (-1, 0),
              (1, 0), (-1, -1), (0, -1), (1, -1)}


def NumberOfNeighbors(r, c, g):
    neighbors = 0
    for dr, dc in Directions:
        new_r = r
        new_c = c
        while True:
            new_r += dr
            new_c += dc
            if 0 <= new_r < shape[0] and 0 <= new_c < shape[1]:  # valid space on grid
                if grid[new_r][new_c] != ".":
                    if grid[new_r][new_c] == "#":
                        neighbors += 1
                    break
            else:
                break

    return neighbors


#print(NumberOfNeighbors(4, 3, grid))


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

            if seat == "#" and neighbors >= 5:
                new_grid[row][col] = "L"

    #print(new_grid)
    if np.array_equal(grid, new_grid):
        break
    grid = new_grid


count = 0
for row in grid:
    for val in row:
        if val == "#":
            count += 1

print(count)
