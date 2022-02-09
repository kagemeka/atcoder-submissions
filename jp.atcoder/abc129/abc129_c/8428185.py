
# 2019-11-14 10:01:24(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

mod = 10 ** 9 + 7
def main():
    n, m, *a = [int(x) for x in sys.stdin.read().split()]

    safe = sorted(set(range(1,n+1)) - set(a))
    dp = [0] * (n + 2) # dp[i+1]: i段目までいくパターン数
    dp[0] = 0  # -1段目にはいけない
    dp[1] = 1  # 初期条件(0段目にいる)
    for i in safe:
        dp[i+1] = (dp[i] + dp[i-1]) % mod

    print(dp[-1])

if __name__ == "__main__":
    main()
