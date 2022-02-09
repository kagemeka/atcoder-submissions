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
    if list(s) == list(reversed(s)):
        return True
    return False

def main():
    s = sys.stdin.readline().rstrip()

    if not is_palindrome_in(s):
        print(-1)
        sys.exit()

    s = collections.deque(s)

    count = 0
    while len(s) > 1:
        if s[0] == 'x':
            if s[-1] == 'x':
                s.popleft(); s.pop()
            else:
                s.popleft()
                count += 1
        else:
            if s[-1] != 'x':
                s.popleft(); s.pop()
            else:
                s.pop()
                count += 1

    print(count)

if __name__ == "__main__":
    main()
