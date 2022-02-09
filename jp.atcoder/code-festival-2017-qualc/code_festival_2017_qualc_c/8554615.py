# 2019-11-21 01:26:03(JST)
import sys
import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r, insort_left as in_l
# import itertools
# from functools import reduce
# import operator as op
# import re
# import heapq
# import array
# from scipy.misc import comb # (default: exact=False)
# import numpy as np

def is_palindrome_in(s):
    s = s.replace('x', '')
    if s == ''.join(reversed(s)):
        return True
    else:
        return False

def main():
    s = sys.stdin.readline().rstrip()

    if not is_palindrome_in(s):
        print(-1)
        exit()

    s = collections.deque(s)
    print(s)
    count = 0
    i, j = 0, 0
    while i < len(s) - 1 - j:
        if s[i] == 'x':
            if s[-1-j] == 'x':
                pass
            else:
                s.insert(len(s)-j, 'x')
                count += 1
        else:
            if s[-1-j] == 'x':
                s.insert(i, 'x')
                count += 1

        i += 1
        j += 1

    print(count)


if __name__ == "__main__":
    main()
