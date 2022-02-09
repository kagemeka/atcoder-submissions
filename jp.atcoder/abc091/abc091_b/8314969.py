#                         author:  kagemeka
#                         created: 2019-11-06 22:04:18(JST)
import sys
import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    l = sys.stdin.read().split()
    n = int(l[0])
    m = int(l[n+1])
    a = collections.Counter(l[1:n+1])
    b = collections.Counter(l[n+2:n+m+2])
    for s, c in b.items():
        if s in a:
            a[s] -= c

    ma = max(max(a.values()), 0)
    print(ma)


if __name__ == "__main__":
    # execute only if run as a script
    main()
