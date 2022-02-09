#                         author:  kagemeka
#                         created: 2019-11-07 12:33:44(JST)
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
    a, b, c, x, y = (int(i) for i in sys.stdin.readline().split())
    if a + b <= c * 2:
        cost = a * x + b * y
    elif x >= y:
        atleast = y
        cost = c * atleast * 2
        remainder = x - atleast
        if a <= c * 2:
            cost += a * remainder
        else:
            cost += c * remainder * 2
    else:
        atleast = x
        cost = c * atleast * 2
        remainder = y - atleast
        if b <= c * 2:
            cost += b * remainder
        else:
            cost += c * remainder * 2

    print(cost)

if __name__ == "__main__":
    # execute only if run as a script
    main()
