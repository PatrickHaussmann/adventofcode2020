with open('10/input.txt', 'r') as reader:
    lines = [int(line.strip()) for line in reader if line.strip()]

lines.append(0)  # outlet
lines.append(max(lines)+3)  # laptop

lines.sort()


threes = 0
ones = 0

for i in range(len(lines)-1):
    diff = lines[i+1]-lines[i]
    if diff == 3:
        threes += 1
    if diff == 1:
        ones += 1

print(ones*threes)
