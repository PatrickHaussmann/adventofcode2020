with open('14/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]

instructions = []
tmp = []
mask = ""
for line in lines:
    first, value = line.split(" = ")
    if first == "mask":
        if tmp:
            instructions.append((mask, tmp))
            tmp = []
        mask = value
    elif first.startswith("mem"):
        address = first.split("[")[1][:-1]
        tmp.append((int(address), int(value)))

if tmp:
    instructions.append((mask, tmp))


def applyMask(mask, number):
    oneMask = int(mask.replace("X", "0"), base=2)
    zeroMask = int(mask.replace("X", "1"), base=2)

    return (number & zeroMask) | oneMask


mem = {}

for mask, array in instructions:
    for address, value in array:
        mem[address] = applyMask(mask, value)

print(sum(mem.values()))
