lines = []
with open('02/input.txt', 'r') as reader:
    for line in reader:
        line = line.strip('\n')
        line = line.strip('\t')
        lines.append(line)


n = 0

for line in lines:
    lo = int(line.split(":")[0].split(" ")[0].split("-")[0])
    hi = int(line.split(":")[0].split(" ")[0].split("-")[1])
    char = line.split(":")[0].split(" ")[1]
    password = line.split(":")[1].strip()

    counter = password.count(char)

    a = 0
    if password[lo-1] == char:
        a += 1
    if password[hi-1] == char:
        a += 1

    if a == 1:
        n += 1

print(n)
