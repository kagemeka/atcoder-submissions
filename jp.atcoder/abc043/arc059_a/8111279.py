n = int(input())
ints = [int(num) for num in set(input().split())]
res = []
for x in range(min(ints), max(ints)+1):
    total = 0
    for num in ints:
        total += (x - num)**2

    res.append(total)

ans = min(res)
print(ans)
