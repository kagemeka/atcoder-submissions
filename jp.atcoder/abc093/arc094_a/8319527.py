#                         author:  kagemeka
#                         created: 2019-11-07 02:35:07(JST)
import sys
# import collections
import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    *n, = (int(x) for x in sys.stdin.readline().split())
    n.sort()
    diff = n[2] * 2 - n[1] - n[0]
    print(diff // 2 if diff % 2 == 0 else math.ceil(diff / 2) + 1)



if __name__ == "__main__":
    # execute only if run as a script
    main()
