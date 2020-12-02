import math

numbers = []
with open('01/input.txt', 'r') as reader:
    for line in reader:
        line = line.strip('\n')
        line = line.strip('\t')
        numbers.append(int(line))
numbers.sort()
length = len(numbers)

for i in range(length):
    for j in range(length):
        if i != j:
            sum = numbers[i] + numbers[j]
            if sum == 2020:
                print(numbers[i], numbers[j])
