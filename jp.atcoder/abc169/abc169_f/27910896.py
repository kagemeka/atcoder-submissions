import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    n, s = map(int, input().split())
    k = 1 << 12
    a = list(map(int, input().split()))

    dp = np.zeros(k, dtype=np.int64)
    dp[0] = 1
    MOD = 998_244_353
    for x in a:
        cache = dp.copy()
        dp[x:] += dp[:-x]
        dp += cache
        dp %= MOD
    print(dp[s])

main()
