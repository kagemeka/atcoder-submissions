#                         author:  kagemeka
#                         created: 2019-11-06 21:30:22(JST)
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
    n, m = (int(x) for x in sys.stdin.read().split())
    if n == 1 and m == 1:
        ans = 0
    elif n == 1:
        ans = m - 2
    elif m == 1:
        ans = n - 2
    else:
        ans = (n - 2) * (m - 2)

    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
