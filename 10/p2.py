with open('10/input.txt', 'r') as reader:
    lines = [int(line.strip()) for line in reader if line.strip()]

lines.append(0)  # outlet
lines.append(max(lines)+3)  # laptop

lines.sort()


dp = [1]
for i in range(1, len(lines)):
    ans = 0
    for j in range(i):
        if lines[j] + 3 >= lines[i]:
            ans += dp[j]
    dp.append(ans)

print(dp[-1])
