# 予めsx, syを全て計算しておく
# このとき漸化式を使えば毎回全ての話を求める必要がない

mod = int(1e9+7)
n, m = [int(num) for num in input().split()]

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]


sx = [0] * n
sx[0] = x[0]
for i in range(n-1):
    sx[i+1] = sx[i] + x[i+1]
sxd = 0
for i in range(n-1):
    sxd += ((sx[n-1] - sx[i]) - x[i] * ((n-1) - (i+1) + 1)) #% mod

sy = [0] * m
sy[0] = y[0]
for k in range(m-1):
    sy[k+1] = sy[k] + y[k+1]
syd = 0
for k in range(m-1):
    syd += ((sy[m-1] - sy[k]) - y[k] * ((m-1) - (k+1) + 1)) #% mod

ans = ((sxd % mod) * (syd % mod)) % mod

print(ans)
