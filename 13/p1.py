with open('13/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]

timestamp = int(lines[0])
busses = [int(id) for id in lines[1].split(',') if id != "x"]

time = timestamp
found = False
while not found:
    for bus in busses:
        if time % bus == 0:
            found = bus
            break
    else:
        time += 1


print((time-timestamp) * bus)
