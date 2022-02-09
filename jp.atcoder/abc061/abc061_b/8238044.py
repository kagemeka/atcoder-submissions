n, m = [int(x) for x in input().split()]

res = []
for _ in range(m):
    res += [int(x) for x in input().split()]

for j in range(1, n+1):
    print(res.count(j))
