with open('15/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]

starting_number = [int(n) for n in lines[0].split(",")]

spoken = {}
for i, number in enumerate(starting_number[:-1]):
    spoken[number] = i+1

last = starting_number[-1]

max_number = 2020       # Part 1
max_number = 30000000   # Part 2

for i in range(len(starting_number)+1, max_number+1):
    if last in spoken:
        number = (i-1) - spoken[last]
    else:
        number = 0

    spoken[last] = i-1
    last = number

print(number)
