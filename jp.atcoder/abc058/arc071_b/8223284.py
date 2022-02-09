mod = int(1e9+7)
n, m = [int(num) for num in input().split()]

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]

sx = [0] * n
sx[0] = x[0]
for i in range(n-1):
    sx[i+1] = sx[i] + x[i+1]
sx.reverse()
sxd = 0
for i in range(n-1):
    sxd += sx[-i - 2] - x[i] * (n - 1 - i)

sy = [0] * m
sy[0] = y[0]
for k in range(m-1):
    sy[k+1] = sy[k] + y[k+1]
sy.reverse()
syd = 0
for k in range(m-1):
    syd += sy[-k - 2] - y[k] * (m - 1 - k)

ans = ((sxd % mod) * (syd % mod)) % mod

print(ans)
