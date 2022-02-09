#                         author:  kagemeka
#                         created: 2019-11-07 00:57:57(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    n = int(sys.stdin.readline().rstrip())
    a = [0] + [int(x) for x in sys.stdin.readline().split()] + [0]
    way = 0
    for i in range(n+1):
        way += abs(a[i+1] - a[i])

    for i in range(1, n+1):
        pre, cur, nex = a[i-1], a[i], a[i+1]
        if pre <= cur <= nex or pre >= cur >= nex:
            ans = way
        elif pre <= nex <= cur or pre >= nex >= cur:
            ans = way - abs(nex - cur) * 2
        elif cur <= pre <= nex or cur >= pre >= nex:
            ans = way - abs(cur - pre) * 2

        print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
