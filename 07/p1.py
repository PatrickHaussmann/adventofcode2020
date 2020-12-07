with open('07/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]


def stripAll(array):
    result = []
    for item in array:
        result.append(item.strip())
    return result


for i in range(len(lines)):
    tmp = lines[i].replace("bags", "").replace("bag", "")
    tmp = tmp.replace(" .", "").split("contain")
    lines[i] = [tmp[0].strip(), stripAll(tmp[1].split(","))]

colors = {}

for line in lines:
    if line[1] == ['no other']:
        childs = {}
    else:
        childs = {}
        for child in line[1]:
            number, color = child.split(" ", 1)
            childs[color] = int(number)
    colors[line[0]] = childs


bags = ["shiny gold"]

n = 0
while bags:
    search = bags.pop()
    if search in colors:
        del colors[search]
    else:
        continue

    for color, childs in colors.items():
        if search in childs:
            bags.append(color)
            n += 1

print(n-1)
