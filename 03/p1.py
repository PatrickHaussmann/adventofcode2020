import numpy as np

lines = []
with open('03/input.txt', 'r') as reader:
    for line in reader:
        line = line.strip('\n')
        line = line.strip('\t')
        lines.append([char for char in line])

matrix = np.array(lines)
rows, cols = shape = np.shape(matrix)
#print(matrix)


def checkiftree(r, c):
    c = c % cols
    return matrix[r][c] == "#"


n = 0
j = 0
for i in range(rows):
    if checkiftree(i, j):
        n += 1
    j += 3

print(n)
