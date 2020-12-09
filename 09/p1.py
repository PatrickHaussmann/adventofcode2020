with open('09/input.txt', 'r') as reader:
    lines = [int(line.strip()) for line in reader if line.strip()]

preamble = 25


def isSumOfTwoElements(number, array):
    array.sort()
    
    for element in array:
        if (number-element) in array:
            return True
    return False


for i in range(preamble, len(lines)):
    b = isSumOfTwoElements(lines[i], lines[i-preamble:i])
    if not b:
        print(lines[i])
        break
