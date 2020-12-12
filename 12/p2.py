with open('12/input.txt', 'r') as reader:
    lines = [[line.strip()[:1], int(line.strip()[1:])]
             for line in reader if line.strip()]

directions = {"N": 1+0j, "E": 0+1j, "S": -1+0j, "W": 0-1j}
waypoint = 10 * directions["E"] + directions["N"]
taxicab = 0+0j

for instruction, value in lines:
    if instruction == "F":
        taxicab += waypoint*value
    elif instruction == "L":
        waypoint *= (0+1j) ** (-value/90)
    elif instruction == "R":
        waypoint *= (0+1j) ** (value/90)
    else:
        waypoint += directions[instruction]*value

dist = int(abs(taxicab.imag)+abs(taxicab.real))

print(taxicab, dist)
