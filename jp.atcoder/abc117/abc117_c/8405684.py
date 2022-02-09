# 2019-11-12 13:20:54(JST)
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
    n, m, *x = (int(i) for i in sys.stdin.read().split())
    x.sort()
    if n >= m:
        print(0)
        sys.exit()

    dist = []
    # 座標順に並び替えて、m-1個の区間の距離を列挙していく
    for i in range(m-1):
        dist.append(x[i+1] - x[i])

    # n個は初期で設置するので、それらを起点として((m-1)-(n-1))回ポイント間を移動した場合、ポイントが重複しないように移動した時の距離の合計の最小値
    # ポイントの間の距離の組み合わせを列挙して、それらのうち長い方からn-1個の組み合わせの区間は移動するべきではないと考える。
    # イメージ的には隣り合う距離が長い２点の組み合わせから順にコマを置いていけばいい
    dist.sort()
    ans = sum(dist[:(m-1)-(n-1)])

    print(ans)

if __name__ == "__main__":
    main()
