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

odd_position = 'RUD'
even_position = 'LUD'

def main():
    s = 'S' + sys.stdin.readline().rstrip() # S: no meaning
    for i in range(1, len(s)-1+1):
        if i % 2 != 0:
            if s[i] in odd_position:
                continue
            else:
                ans = 'No'
                break
        else:
            if s[i] in even_position:
                continue
            else:
                ans = 'No'
                break
    else:
        ans = 'Yes'

    print(ans)



if __name__ == "__main__":
    main()
