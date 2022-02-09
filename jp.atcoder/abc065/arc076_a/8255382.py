import sys
input = sys.stdin.readline
from math import factorial
mod = 10 ** 9 + 7

N, M = [int(x) for x in input().split()]
if abs(N - M) >= 2: ans = 0
else: ans = (factorial(N) % mod * factorial(M) % mod) % mod
if N == M: ans *= 2
print(ans % mod)
