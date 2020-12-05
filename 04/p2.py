import numpy as np

lines = []
longline = ''
with open('04/input.txt', 'r') as reader:
    for line in reader:
        longline += line

lines = longline.split('\n\n')

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", " ")
    lines[i] = lines[i].split(" ")

for line in lines:
    for i in range(len(line)):
        line[i] = key, value = line[i].split(":")

needed = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

hex = [char for char in "0123456789abcdef"]
numbers = [char for char in "0123456789"]


def valid(key, value):
    if key == "byr":
        if len(value) != 4:
            return False
        if 1920 <= int(value) <= 2002:
            return True
    if key == "iyr":
        if len(value) != 4:
            return False
        if 2010 <= int(value) <= 2020:
            return True
    if key == "eyr":
        if len(value) != 4:
            return False
        if 2020 <= int(value) <= 2030:
            return True
    if key == "hgt":
        if value[-2:] == "cm":
            if 150 <= int(value[:-2]) <= 193:
                return True
        if value[-2:] == "in":
            if 59 <= int(value[:-2]) <= 76:
                return True
    if key == "hcl":
        if len(value) != 7:
            return False
        if value[0] != "#":
            return False
        for i in range(1, 7):
            if value[i] not in hex:
                return False
        return True
    if key == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
    if key == "pid":
        if len(value) != 9:
            return False
        for i in range(9):
            if value[i] not in numbers:
                return False
        return True

    return False


n = 0
for line in lines:
    keys = set()

    for kv in line:
        key = kv[0]
        value = kv[1]
        if valid(key, value):
            keys.add(key)

    # keys.discard("cid")
    if keys == needed:
        n += 1
    print(keys)


print(n)


""" 

ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid(Passport ID) - a nine-digit number, including leading zeroes.
 """
