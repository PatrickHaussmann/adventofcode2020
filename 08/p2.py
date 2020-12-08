with open('08/input.txt', 'r') as reader:
    lines = [[line.strip().split(" ")[0], int(line.strip().split(" ")[1])]
             for line in reader if line.strip()]


def isInfiniteLoop(instructions):
    accumulator = 0
    index = 0
    visited = set()

    while True:
        instruction, argument = instructions[index]

        if index in visited:
            #print("Loop detected: acc="+str(accumulator))
            return True
        else:
            visited.add(index)

        if instruction == "acc":
            accumulator += argument
        elif instruction == "jmp":
            index += argument - 1  # because of increment at bottom of the loop

        index += 1

        if index >= len(instructions):
            print("Terminated: acc="+str(accumulator))
            return False


i = -1 # increment at the beginning of while loop
while i < len(lines):
    i += 1
    instructions = list(lines)
    instruction, argument = instructions[i]
    if instruction == "jmp":
        instructions[i] = ["nop", argument]
    elif instruction == "nop":
        instructions[i] = ["jmp", argument]
    else:
        continue
    
    if not isInfiniteLoop(instructions):
        print(i)
        break
