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
    n, d, x, *a = (int(i) for i in sys.stdin.read().split())
    d -= 1
    c = n
    for i in range(n):
        c += d // a[i]
    total = c + x
    print(total)


if __name__ == "__main__":
    # execute only if run as a script
    main()
