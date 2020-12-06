lines = []
longline = ''
with open('06/input.txt', 'r') as reader:
    for line in reader:
        longline += line

lines = longline.split('\n\n')

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

s = 0

for line in lines:
    s += len(set(line))


print(s)
