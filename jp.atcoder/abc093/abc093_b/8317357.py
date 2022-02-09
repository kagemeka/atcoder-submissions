#                         author:  kagemeka
#                         created: 2019-11-07 02:35:07(JST)
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
    a, b, k = (int(i) for i in sys.stdin.readline().split())
    ab = list(range(a, b+1))
    if k * 2 >= len(ab):
        res = ab
    else:
        res = ab[:k] + ab[-k:]
    for r in res:
        print(r)


if __name__ == "__main__":
    # execute only if run as a script
    main()
