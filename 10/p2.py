with open('10/input.txt', 'r') as reader:
    lines = [int(line.strip()) for line in reader if line.strip()]

lines.append(0)  # outlet
lines.append(max(lines)+3)  # laptop

lines.sort()

groupsOfOnes = []
ones = 0

for i in range(len(lines)-1):
    diff = lines[i+1]-lines[i]
    if diff == 3 and ones != 0:
        groupsOfOnes.append(ones)
        ones = 0
    if diff == 1:
        ones += 1

arrangements = 1
for ones in groupsOfOnes:
    if ones == 1:
        continue
    if ones == 2:
        arrangements *= 2
    if ones == 3:
        arrangements *= 4
    if ones == 4:
        arrangements *= 7

print(arrangements)
