import sys
import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():

    n, *a = (int(x) for x in sys.stdin.read().split())
    c = collections.Counter(a)
    count = 0
    for i, j in c.items():
        if j < i: count += j
        else: count += j - i

    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
