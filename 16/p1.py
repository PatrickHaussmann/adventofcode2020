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


def flatten(array):
    result = []
    for item in array:
        for x in item:
            result.append(x)
    return result


allRanges = flatten(ranges.values())
allTickets = flatten(tickets)


ticket_scanning_error_rate = 0

for ticket in allTickets:
    matched = False
    for Range in allRanges:
        lower, upper = Range
        if Range[0] <= ticket <= Range[1]:
            matched = True
    if not matched:
        ticket_scanning_error_rate += ticket


print(ticket_scanning_error_rate)
