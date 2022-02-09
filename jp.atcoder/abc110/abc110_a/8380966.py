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
    nums = sys.stdin.readline().split()
    nums.sort(reverse=True)
    ans = int(''.join(nums[:2])) + int(nums[2])
    print(ans)

if __name__ == "__main__":
    main()
