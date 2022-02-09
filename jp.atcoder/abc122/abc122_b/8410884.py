# 2019-11-12 22:21:08(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    s = sys.stdin.readline().rstrip()

    all_words = []
    for i in range(1, len(s) + 1):
        for letters in itertools.product('ATCG', repeat=i):
            word = ''.join(letters)
            all_words.append(word)

    for i in range(len(all_words)-1, 0-1, -1):
        if all_words[i] in s:
            print(len(all_words[i]))
            sys.exit()
    print(0)




if __name__ == "__main__":
    main()
