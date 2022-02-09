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
    a, b = (int(x) for x in sys.stdin.read().split())

    count = 0
    for n in range(a, b+1):
        n = str(n)
        if n == n[::-1]:
            count += 1

    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
