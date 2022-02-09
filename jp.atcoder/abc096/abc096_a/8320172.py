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
    a, b = (int(x) for x in sys.stdin.readline().split())
    ans = a if b >= a else a - 1
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
