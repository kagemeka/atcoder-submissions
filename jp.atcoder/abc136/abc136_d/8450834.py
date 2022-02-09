# 2019-11-16 10:55:08(JST)
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
import re

def main():
    # 左がRで右がLとなっている箇所でそれぞれどちらかにあつまる。10^100 は実質無限なので距離が奇数か偶数かで場合わけ
    s = sys.stdin.readline().rstrip() + 'R' # 後々のループ処理のときのことを考えて最後にRを足しておく
    n = len(s) - 1
    all_occurrences_of_rl = [m.start() for m in re.finditer('RL', s)]

    counts = [0 for _ in range(n)]
    left = 0
    for i in range(len(all_occurrences_of_rl)):
        right = all_occurrences_of_rl[i] + 1
        while s[right+1] == 'L': # 次がLだったら右端を拡張していく
            right += 1

        r_count = 1 + (all_occurrences_of_rl[i] - left) // 2 + (right - all_occurrences_of_rl[i]) // 2
        l_count = (right - left + 1) - r_count
        counts[all_occurrences_of_rl[i]] = r_count
        counts[all_occurrences_of_rl[i] + 1] = l_count

        left = right + 1

    for i in range(n):
        print(counts[i], end=' ')


if __name__ == "__main__":
    main()
