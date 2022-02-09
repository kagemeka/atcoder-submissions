# 2019-11-10 15:45:20(JST)
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
    S, T = sys.stdin.read().split()

    convert = dict()

    flag = True
    for s, t in zip(S, T):
        if s in convert and convert[s] != t:
            flag = False
            break
        convert[s] = t

    # ここまでで対応表が完成
    # あとは異なる文字が同じ文字に変換されていないか確認
    after = convert.values()
    if len(after) != len(set(after)):
        flag = False


    print('Yes' if flag else 'No')

if __name__ == "__main__":
    main()
