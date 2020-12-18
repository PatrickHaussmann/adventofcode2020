import itertools

with open('17/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]


active = set()

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == "#":
            #active.add((i, j, 0))    # Part 1
            active.add((i, j, 0, 0))  # Part 2

del i, j, line, lines, val, reader


def neighbors(pos):
    ranges = [range(coordinate - 1, coordinate + 2) for coordinate in pos]
    for cell in itertools.product(*ranges):
        if not max(map(lambda a, b: abs(a-b), pos, cell)) == 0:
            yield cell


def number_neighbors(pos, active_set):
    result = 0
    for cell in neighbors(pos):
        if cell in active_set:
            result += 1
    return result


steps = 6
for step in range(steps):
    new = set()
    transpose = list(zip(*active))
    minimum = list(map(min, transpose))
    maximum = list(map(max, transpose))

    ranges = [range(mi - 1, ma + 2) for mi, ma in zip(minimum, maximum)]
    for pos in itertools.product(*ranges):
        n = number_neighbors(pos, active)
        if pos in active:
            if n in [2, 3]:
                new.add(pos)
        else:
            if n == 3:
                new.add(pos)

    active = new

print(len(active))
