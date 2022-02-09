import typing
import sys
import numpy as np

def main() -> typing.NoReturn:
    n, s = map(int, input().split())

    a = list(map(int, input().split()))
    MOD = 998_244_353
    dp = np.zeros(s + 1, np.int64)
    dp[0] = 1
    for x in a:
        tmp = dp.copy()
        dp *= 2
        dp[x:] += tmp[:-x]
        dp %= MOD
    print(dp[s])

main()
