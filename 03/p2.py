import numpy as np
import operator
from functools import reduce

lines = []
with open('03/input.txt', 'r') as reader:
    for line in reader:
        line = line.strip('\n')
        line = line.strip('\t')
        lines.append([char for char in line])

matrix = np.array(lines)
rows, cols = shape = np.shape(matrix)
# print(matrix)

slopes = [[1, 1],
          [3, 1],
          [5, 1],
          [7, 1],
          [1, 2]]


#slopes = [[3, 1]]


def checkiftree(r, c):
    c = c % cols
    return matrix[r][c] == "#"


def mul(lst):
    """Like sum(), but for multiplication."""
    return reduce(operator.mul, lst, 1)  # NOQA

nums = []
for slope in slopes:
    n = 0
    j = 0
    for i in range(0, rows, slope[1]):
        if checkiftree(i, j):
            n += 1
        j += slope[0]
    nums.append(n)

print(nums)
print(mul(nums))