# 2019-11-14 17:27:23(JST)
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
    W, H, x, y = [int(i) for i in sys.stdin.readline().split()]

    # どこに座標をとっても必ず中心を通る直線で半分になる
    # 座標が中心の場合のみ、長方形を半分に分断する直線が無数に存在する
    area = W * H / 2
    if W == x * 2 and H == y * 2:
        sign = '1'
    else:
        sign = '0'
    print(area, sign)


if __name__ == "__main__":
    main()
