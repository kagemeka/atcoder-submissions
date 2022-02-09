# 2019-11-16 14:51:41(JST)
import sys
import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
# import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    # 10**5連勤とか超人すぎる
    n, m = [int(x) for x in sys.stdin.readline().split()]

    job_list = dict((i, collections.deque()) for i in range(1, m+1))
    for _ in range(n):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if a <= m:
            job_list[a].append(b)

    # 同じ日にできる仕事が二つ以上あったとして、
    # 第一に報酬が最も高い仕事をその日のシフトに入れる
    # それよりも前の日に空きがあれば残りの仕事を報酬の高い順に入れる
    # 空きがなかった場合、前日以前にやる仕事の中で最も報酬の低いものよりも、残りの仕事のなかで
    # 最も報酬の高いものの方が良ければ、その日の予定をを更新する。

    day_rewards = [0 for _ in range(m+1)] # 期限当日は報酬ゼロとして

    for i in range(m, 0, -1):
        while job_list[i]:
            if i < m:
                mi = min(day_rewards[i:])
                if mi < max(job_list[i]):
                    day_rewards[day_rewards.index(mi, i)] = max(job_list[i])
                    job_list[i].remove(max(job_list[i]))
                else:
                    break
            else:
                break

    print(sum(day_rewards))


if __name__ == "__main__":
    main()
