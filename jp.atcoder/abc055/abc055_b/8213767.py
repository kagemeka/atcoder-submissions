from math import factorial
mod = 10 ** 9 + 7
n = int(input())

ans = factorial(n)
print(ans % mod)
