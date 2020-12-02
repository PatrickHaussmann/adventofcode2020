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
        for k in range(length-1, -1, -1):
            if i != j and j != k and k != i:
                sum = numbers[i] + numbers[j] + numbers[k]
                if sum == 2020:
                    print(numbers[i], numbers[j], numbers[k],
                          numbers[i] * numbers[j] * numbers[k])
