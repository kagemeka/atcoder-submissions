# 2019-11-13 21:06:16(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    on_off_patterns = [''.join(pattern) for pattern in itertools.product('01', repeat=n)]

    bulbs = [[int(x) for x in sys.stdin.readline()[1:].split()] for _ in range(m)]
    p = [int(x) for x in sys.stdin.readline().split()]

    combinations = 0
    for i in range(2**n):
        pattern = on_off_patterns[i]
        for j in range(m):
            switches = bulbs[j]
            on_count = 0
            for switch in switches:
                if pattern[switch-1] == '1':
                    on_count += 1
            if on_count % 2 == p[j]:
                continue
            else:
                break
        else:
            combinations += 1

    print(combinations)

    # enumerate on/off-patters by using binary number.


if __name__ == "__main__":
    main()
