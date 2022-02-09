# 2019-11-10 20:23:41(JST)
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
    n = int(sys.stdin.readline().rstrip())
    info = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

    # 基準を決める
    for i in range(n):
        if info[i][2] >= 1:
            x0, y0, h0 = info[i][0], info[i][1], info[i][2]
            break
    # else: すべてのhは h = 0

    for x in range(101):
        for y in range(101):
            H = h0 + abs(x - x0) + abs(y - y0)
            for i in range(n):   # 中心(x, y, H)が条件を満たしているか確認する
                h = max(H - abs(x - info[i][0]) - abs(y - info[i][1]), 0)
                if h != info[i][2]: #　本当に中心なら同じ値になるはず
                    break     # そうでないならこれは正しくない
            else:  # 全ての座標に対して条件を満たしていたなら
                res = [x, y, H]
                for i in range(3):
                    res[i] = str(res[i])
                print(' '.join(res))
                sys.exit() # 中心は一意に決まるので見つかったらそれ以上調べる必要ない



if __name__ == "__main__":
    main()
