from math import factorial
mod = int(1e9+7)
n = int(input())

ans = factorial(n)
print(ans % mod)
