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
import heapq

def main():
    # 10**5連勤とか超人すぎる
    n, m = [int(x) for x in sys.stdin.readline().split()]

    job_list = dict((i, list()) for i in range(1, m+1))
    for _ in range(n):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if a <= m:
            job_list[a].append(b)

    schedule = [0 for _ in range(m+1)] # 当日は報酬0
    q = []
    for i in range(1, m+1):
        for reward in job_list[i]: # 期限i日前にできる仕事の報酬一覧をheqp queueに入れる
            heapq.heappush(q, -reward)
            # あとで最大値を取り出すために-1かける(heappop()で取り出せるのは最小値)

        if q: # その日できる仕事が一つでもあれば
            # 報酬の最小値(マイナスなので元々の最大値)を取り出して-1をかけ、scheduleにいれる
            schedule[i] = -heapq.heappop(q) # 戻り値を返すと同時にsheduleにいれた報酬値はqから除いている
        else: # できる仕事がなければ
            pass  # その日の報酬は0のまま

    print(sum(schedule))


if __name__ == "__main__":
    main()
