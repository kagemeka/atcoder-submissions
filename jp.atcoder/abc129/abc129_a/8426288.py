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
    times = [int(x) for x in sys.stdin.readline().split()]
    times.sort()
    ans = sum(times[:2])
    print(ans)




if __name__ == "__main__":
    main()
