# 2019-11-18 17:34:23(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np

weather = ['Sunny', 'Cloudy', 'Rainy']
mod = 3

def main():
    today = sys.stdin.readline().rstrip()

    tomorrow = weather[(weather.index(today)+1)%mod]
    print(tomorrow)

if __name__ == "__main__":
    main()
