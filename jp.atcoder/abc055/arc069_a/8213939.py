n, m = [int(x) for x in input().split()]

if 2 * n > m:
    res = m // 2
else:
    res = n + (m - 2 * n) // 4

print(res)
