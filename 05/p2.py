lines = []
with open('05/input.txt', 'r') as reader:
    for line in reader:
        line = line.strip('\n')
        line = line.strip('\t')
        lines.append(line)

ids = []

for line in lines:
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    id = row * 8 + col
    ids.append(id)

ids.sort()

for id in range(ids[0],ids[-1]+1):
    if id not in ids:
        print(id)
