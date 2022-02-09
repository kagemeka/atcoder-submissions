import sys
import collections
# import math
# import string
import bisect
# import re
# import itertools
# import statistics

def main():
    n, k, *a = (int(x) for x in sys.stdin.read().split())

    c = collections.Counter(a)
    diffs = len(c)
    if diffs <= k: print(0); exit()
    remainder = diffs - k
    count = 0
    l = sorted(c.values())
    for i in range(1, n+1):
        b = bisect.bisect_right(l, i) - bisect.bisect_left(l, i)
        if remainder - b >= 0:
            count += b * i
            remainder -= b
        else:
            count += remainder * i
            break

    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
