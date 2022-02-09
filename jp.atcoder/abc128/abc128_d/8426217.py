# 2019-11-13 21:06:16(JST)
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
    n, k, *v = [int(x) for x in sys.stdin.read().split()]

    ma = 0
    for a in range(min(n, k)+1):
        for b in range(min(n, k)-a+1):
            take = v[:a] + v[-b:] if b != 0 else v[:a]
            take.sort()

            if a + b == 0:
                optimum_sum = 0
            else:
                for i in range(min(k-(a+b), a+b)-1, -1, -1):
                    if take[i] > 0:
                        continue
                    else:
                        optimum_sum = sum(take[i+1:])
                        break
                else:
                    optimum_sum = sum(take)

            ma = max(ma, optimum_sum)

    print(ma)

if __name__ == "__main__":
    main()
