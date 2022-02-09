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
        # s = f'#{sys.stdin.readline().rstrip()}#'
        s = '#' + sys.stdin.readline().rstrip() + '#'
        grid.append(s)
    grid.append('#' * (W + 2))

    lighted_squares = []
    for h in range(1, H+1):
        for w in range(1, W+1):
            if grid[h][w] == '#':
                lighted_squares.append(0)
            else:
                count = 1
                for j in range(w-1, -1, -1):
                    if grid[h][j] == '.':
                        count += 1
                        continue
                    else:
                        break
                for j in range(w+1, W+2):
                    if grid[h][j] == '.':
                        count += 1
                        continue
                    else:
                        break
                for i in range(h-1, -1, -1):
                    if grid[i][w] == '.':
                        count += 1
                        continue
                    else:
                        break
                for i in range(h+1, H+2):
                    if grid[i][w] == '.':
                        count += 1
                        continue
                    else:
                        break
                lighted_squares.append(count)

    print(max(lighted_squares))




if __name__ == "__main__":
    main()
