# 2019-11-16 14:51:41(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    job_list = []
    for _ in range(n):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if a <= m:
            job_list.append(tuple([a, b]))

    job_list.sort(reverse=True, key=lambda x: x[1])
    rewards = [0 for _ in range(m+1)]
    count = 0
    for i in range(len(job_list)):
        for j in range(job_list[i][0], m+1):
            if rewards[j] == 0:
                rewards[j] = job_list[i][1]
                count += 1
                break
            else:
                continue
        if count == m:
            break

    print(sum(rewards))


if __name__ == "__main__":
    main()
