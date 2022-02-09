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

def main():
    H, W = [int(x) for x in sys.stdin.readline().split()]
    grid = ['#' * (W + 2)]
    for _ in range(H):
        s = '#' + sys.stdin.readline().rstrip() + '#'
        grid.append(s)
    grid.append('#' * (W + 2))

    l, r, u, d = [[[0 for _ in range(W+2)] for _ in range(H+2)] for _ in range(4)]
    for i in range(1, H+1):
        for j in range(1, W+1):
            l[i][j] = l[i][j-1] + 1 if grid[i][j] == '.' else 0
            r[i][-j-1] = r[i][-j-1+1] + 1 if grid[i][-j-1] == '.' else 0
            u[i][j] = u[i-1][j] + 1 if grid[i][j] == '.' else 0
            d[-i-1][j] = d[-i-1+1][j] + 1 if grid[-i-1][j] == '.' else 0

    lighted_squares = []
    for h in range(1, H+1):
        for w in range(1, W+1):
            if grid[h][w] == 'w':
                lighted_squares.append(0)
            else:
                lighted_squares.append(l[h][w] + r[h][w] + u[h][w] + d[h][w] - 3)

    ans = max(lighted_squares)
    print(ans)


if __name__ == "__main__":
    main()
