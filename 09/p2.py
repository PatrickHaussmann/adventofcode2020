with open('09/input.txt', 'r') as reader:
    lines = [int(line.strip()) for line in reader if line.strip()]

target = 26796446

for i in range(len(lines)):
    sum = 0
    offset = 0
    while sum < target:
        sum += lines[i+offset]
        if sum == target and offset != 0:
            print(min(lines[i:i+offset+1]) + max(lines[i:i+offset+1]))
            break
        offset += 1
