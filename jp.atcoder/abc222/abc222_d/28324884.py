import typing
import numpy as np
import sys

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a = np.array(a)
    # b = np.array(b)

    MOD = 998_244_353
    k = 1 << 12
    dp = np.zeros(k, dtype=np.int64)
    dp[0] = 1
    for i in range(n):
        dp = dp.cumsum() % MOD
        dp[:a[i]] = 0
        dp[b[i] + 1:] = 0
    print(dp.sum() % MOD)

main()
