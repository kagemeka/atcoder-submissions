#                         author:  kagemeka
#                         created: 2019-11-07 11:52:43(JST)
import sys
# import collections
# import math
# import string
import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator

def main():
    n, m, x, *a = (int(i) for i in sys.stdin.read().split())
    th_x  = bisect.bisect_left(a, x)
    cost = min(th_x, m - th_x)
    print(cost)



if __name__ == "__main__":
    # execute only if run as a script
    main()
