#                         author:  kagemeka
#                         created: 2019-11-07 11:52:43(JST)
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
    a, b, x = (int(i) for i in sys.stdin.readline().split())
    print('YES' if x >= a and b >= x - a else 'NO')


if __name__ == "__main__":
    # execute only if run as a script
    main()
