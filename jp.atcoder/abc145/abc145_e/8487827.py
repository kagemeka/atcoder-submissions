# 2019-11-16 21:01:15(JST)
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

def main():
    N,T = [int(x) for x in sys.stdin.readline().split()]
    time, deliciousness = [], []
    for _ in range(N):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        time.append(a)
        deliciousness.append(b)

    dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
    for i in range(N):
        for t in range(T+1):
            if t >= time[i]:
                dp[i+1][t] = max(dp[i][t], dp[i][t-time[i]] + deliciousness[i])
            else:
                dp[i+1][t] = dp[i][t]

    print(dp[N][T])

if __name__ == "__main__":
    main()
