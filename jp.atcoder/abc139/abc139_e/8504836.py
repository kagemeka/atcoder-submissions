# 2019-11-17 20:44:23(JST)
import sys
import collections
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


def main():
    n = int(sys.stdin.readline().rstrip())
    table = [None] + [collections.deque(int(x) for x in sys.stdin.readline().split()) for _ in range(n)]

    for day in range(1, n * (n - 1) // 2 + 2):
        already_played = []
        finished_count = 0
        for i in range(1, n+1):
            if not table[i]:
                finished_count += 1
                continue
            if i in already_played:
                continue
            j = table[i][0]
            if j in already_played:
                continue
            # if not table[j]:
            #     continue
            if table[j][0] == i:
                already_played += [i, j]
                table[j].popleft()
                table[i].popleft()
        if not already_played:
            if finished_count == n:
                print(day - 1)
                sys.exit()
            print(-1)
            sys.exit()





if __name__ == "__main__":
    main()
