mod = int(1e9+7)
n, m = [int(num) for num in input().split()]

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]

sumx = 0
for i in range(n-1):
    sumx += (sum(x[i+1:]) - x[i] * ((n-1) - (i+1) + 1)) % mod
sumy = 0
for k in range(m-1):
    sumy += (sum(y[k+1:]) - y[k] * ((m-1) - (k+1) + 1)) % mod

ans = ((sumx % mod) * (sumy % mod)) % mod

print(ans)
