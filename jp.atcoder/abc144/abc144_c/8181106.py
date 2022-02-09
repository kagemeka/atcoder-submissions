import math

n = int(input())

ans  = 10 ** 7
for i in range(1, math.floor(math.sqrt(n)) + 1):
    if n%i != 0:
        continue
    j = n/i
    ans = min(ans, i+j-2)

print(ans)
