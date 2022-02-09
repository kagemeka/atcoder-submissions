from sys import stdin
n, *a = map(int, stdin.read().split())
c2, c4 = 0, 0
for i in a:
    if i % 2 == 0: c2 += 1
    if i % 4 == 0: c4 += 1

if c4 >= len(a) // 2: ans = "Yes"
elif (len(a) - c4 * 2) == (c2 - c4): ans = "Yes"
else: ans = "No"

print(ans)
