with open('08/input.txt', 'r') as reader:
    lines = [[line.strip().split(" ")[0], int(line.strip().split(" ")[1])]
             for line in reader if line.strip()]

accumulator = 0
index = 0

visited = set()

while True:
    instruction, argument = lines[index]

    if index in visited:
        print(accumulator)
        break
    else:
        visited.add(index)

    if instruction == "acc":
        accumulator += argument
    elif instruction == "jmp":
        index += argument -1 # because of increment at bottom of the loop

    index += 1
