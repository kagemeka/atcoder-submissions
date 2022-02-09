#                         author:  kagemeka
#                         created: 2019-11-07 13:09:56(JST)
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
    *n, k = (int(x) for x in sys.stdin.read().split())
    n.sort()
    total = n[0] + n[1] + n[2] * 2 ** k
    print(total)


if __name__ == "__main__":
    # execute only if run as a script
    main()
