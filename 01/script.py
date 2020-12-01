import math

numbers = []
with open('01/input.txt', 'r') as reader:
    for line in reader:
        line = line.strip('\n')
        line = line.strip('\t')
        numbers.append(int(line))
numbers.sort()
length = len(numbers)

numbers = list(reversed(numbers))
half = math.floor(length/2)

for i in range(half):
    for j in range(length-1, half-1, -1):
        sum = numbers[i] + numbers[j]
        if sum > 2020:
            break
        if sum == 2020:
            print(numbers[i], numbers[j], numbers[i] * numbers[j])

# naive, brute-force:
""" for i in range(length):
    for j in range(length):
        sum = numbers[i] + numbers[j]
        if sum == 2020:
            print(numbers[i], numbers[j])
"""