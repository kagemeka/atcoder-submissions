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


def comb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6 # 問題によってNの大きさは変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


def main():
    x, y = [int(x) for x in sys.stdin.readline().split()]
    # n(+1, +2), m(+2, +1)
    n, m = (2 * y - x) / 3, (2 * x - y) / 3

    if n != abs(int(n)) or m != abs(int(m)):
        print(0)
        sys.exit()
    else:
        n, m = int(n), int(m)
        ans = comb(n+m, m, mod)
        print(ans)

if __name__ == "__main__":
    main()
