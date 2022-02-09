# 2019-11-16 14:51:41(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
from bisect import insort_left as in_l
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np
# import heapq

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    job_list = dict((i, list()) for i in range(1, m+1))
    for _ in range(n):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if a <= m:
            job_list[a].append(b)

    schedule = [0 for _ in range(m+1)]
    rewards_of_appliable_jobs = []
    for i in range(1, m+1):
        for reward in job_list[i]:
            in_l(rewards_of_appliable_jobs, reward)
        if rewards_of_appliable_jobs:
            schedule[i] = rewards_of_appliable_jobs[-1]
            rewards_of_appliable_jobs.pop()

    print(sum(schedule))


if __name__ == "__main__":
    main()
