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


n = 0
for line in lines:
    keys = set()

    for kv in line:
        key = kv[0]
        value = kv[1]
        keys.add(key)
    keys.discard("cid")
    if keys == needed: n+=1
    print(keys)


print(n)
