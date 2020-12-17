longline = ''
with open('16/input.txt', 'r') as reader:
    for line in reader:
        longline += line


ranges, myTicket, tickets = longline.split('\n\n')


def formatRange(Range):
    firstRange, secondRange = Range.split(" or ")
    firstRange = [int(x) for x in firstRange.split("-")]
    secondRange = [int(x) for x in secondRange.split("-")]

    return [firstRange, secondRange]


ranges = [Range.strip().split(": ") for Range in ranges.split("\n")]
ranges = {Range[0]: formatRange(Range[1]) for Range in ranges}

myTicket = list(map(int, myTicket.split("\n")[1].split(",")))
tickets = [list(map(int, ticket.split(",")))
           for ticket in tickets.split(":")[1].split("\n") if ticket]

del reader, longline, formatRange, line

# finish extracting the data into a sensible datastructure


def isInRange(field, number):
    Range = ranges[field]
    first, second = Range

    return (first[0] <= number <= first[1]) or (second[0] <= number <= second[1])

# ---


possibleIndex = {field: list(range(len(ranges))) for field in ranges}

for ticket in tickets:
    for i, number in enumerate(ticket):
        matchedSomething = False
        notmatched = []
        for Range in ranges:
            if isInRange(Range, number):
                matchedSomething = True
            else:
                notmatched.append(Range)

        if matchedSomething:
            for m in notmatched:
                possibleIndex[m].remove(i)

del isInRange, Range, i, m, matchedSomething, notmatched, ticket

# print(possibleIndex)

# ---

order = {}

for i in range(len(ranges)): # this algorithm has to loop atmost len(ranges) times - i is not used
    for field, List in possibleIndex.items():
        if not List:
            continue

        for index in order.values():
            if index in List:
                List.remove(index)

        if len(List) == 1:
            order[field] = List[0]
            possibleIndex[field] = None

del possibleIndex, index, List, field, number, i

# print(order)

# ---

result = 1

for field, index in order.items():
    if field.startswith("departure"):
        result *= myTicket[index]

print(result)
