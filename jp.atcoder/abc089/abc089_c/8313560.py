#                         author:  kagemeka
#                         created: 2019-11-06 16:52:04(JST)
import sys
# import collections
import math
# import string
# import bisect
# import re
# import itertools
# import statistics
import functools
import operator

def nCr(n, r):
    r = min(r, n - r)
    return functools.reduce(operator.mul, range(n, n-r, -1), 1) // math.factorial(r)

def main():
    n = int(sys.stdin.readline().rstrip())
    march = {l: 0 for l in 'MARCH'}

    for i in range(n):
        initial = sys.stdin.readline()[0]
        if initial in march:
            march[initial] += 1


    march = {k: v for k, v in march.items() if v != 0}

    if len(march) < 2:
        print(0)
        exit()

    s = sum(march.values())
    total_cmb = nCr(s, 3)

    for c in march.values():
        if c >= 2:
            total_cmb -= nCr(c, 2) * (len(march) - 1)
        if c >= 3:
            total_cmb -= nCr(c, 3)

    print(total_cmb)

if __name__ == "__main__":
    # execute only if run as a script
    main()
