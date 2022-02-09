#                         author:  kagemeka
#                         created: 2019-11-07 13:42:36(JST)
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
    a, b, c, d = (int(x) for x in sys.stdin.readline().split())

    ans = 'No'
    if abs(c - a) <= d:
        ans = 'Yes'
    else:
        if abs(a - b) <= d and abs(c - b) <= d:
            ans = 'Yes'

    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()
