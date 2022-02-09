from itertools import combinations
mod = int(1e9+7)
n, m = [int(num) for num in input().split()]

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]

sumx = 0
for cmb in combinations(x, 2):
    sumx += cmb[1] - cmb[0]

sumy = 0
for cmb in combinations(y, 2):
    sumy += cmb[1] - cmb[0]

ans = (sumx % mod) * (sumy % mod) % mod

print(ans)
