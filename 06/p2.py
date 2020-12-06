lines = []
longline = ''
with open('06/input.txt', 'r') as reader:
    for line in reader:
        longline += line

lines = longline.split('\n\n')

for i in range(len(lines)):
    lines[i] = lines[i].split("\n")


for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = set(lines[i][j])

s = 0
z = None

for line in lines:
    for x in line:
        if z is not None:
            z = x.intersection(z)
        else:
            z = x
    s += len(z)
    z = None

print(s)
