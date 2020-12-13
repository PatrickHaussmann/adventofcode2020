from functools import reduce

# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


with open('13/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]

buses = [[i, int(bus)]
         for i, bus in enumerate(lines[1].split(',')) if bus != "x"]


dividers = [bus[1] for bus in buses]
remainders = [bus - i for i, bus in buses]
result = chinese_remainder(dividers, remainders)

print(result)
