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


def intToBin(number, padding=False):
    result = str(bin(number))[2:]
    if padding:
        result = result.zfill(padding)
    return result


def getAddresses(mask, address):
    oneMask = int(mask.replace("X", "0"), base=2)
    address = address | oneMask
    address = intToBin(address, 36)

    floating = [i for i, char in enumerate(mask) if char == "X"]

    addresses = []
    l = len(floating)

    for b in range(2**l):
        binary = intToBin(b, l)
        a = address
        for i, position in enumerate(floating):
            a = a[:position] + binary[i] + a[position+1:]
        addresses.append(a)

    return addresses


mem = {}

for mask, array in instructions:
    for address, value in array:
        addresses = getAddresses(mask, address)
        for a in addresses:
            mem[int(a, base=2)] = value

print(sum(mem.values()))
