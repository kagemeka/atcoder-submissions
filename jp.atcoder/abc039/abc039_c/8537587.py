# 2019-11-20 20:43:05(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np

keyboard = 'WBWBWWBWBWBW' * 2

def main():
    s = sys.stdin.readline().rstrip()
    ind = keyboard.find(s[:11])
    if ind == 0:
        ans = 'Do'
    elif ind == 2:
        ans = 'Re'
    elif ind == 4:
        ans = 'Mi'
    elif ind == 5:
        ans = 'Fa'
    elif ind == 7:
        ans = 'So'
    elif ind == 9:
        ans = 'Ra'
    elif ind == 11:
        ans == 'Si'

    print(ans)




if __name__ == "__main__":
    main()
