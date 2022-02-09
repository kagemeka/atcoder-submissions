# 2019-11-15 13:51:51(JST)
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
    # x1 を求めると、連鎖的にxnまで求められる
    # n種類の降った量(x1, x2,...,xn)を求めるのに、それぞれのDとxを使ってちょうどn個の一次不定方程式が作れるので、解はただ一つの組みが存在する
    # nは必ず奇数
    n, *a = [int(x) for x in sys.stdin.read().split()]
    x0 = 0
    for i in range(n):
        if i % 2 == 0:
            x0 += a[i]
        else:
            x0 -= a[i]
    x0 //= 2 # 2x の量が一つの山にふる
    x = [x0]
    for i in range(1, n):
        xi = a[i-1] - x[i-1]
        x.append(xi)

    # xは半分の量のlistなので2倍して出力する
    for i in range(n):
        print(x[i] * 2, end=' ')

if __name__ == "__main__":
    main()
