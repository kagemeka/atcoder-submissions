# 2019-11-19 10:28:31(JST)
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



INF = 10 ** 12

# V: number of vertices, cost: graph(dist[u][v] / time[u][v] / ...)
def warshall_floyd(V, cost):
    min_cost = cost
    for w in range(1, V+1): # way-point
        for s in range(1, V+1): # start
            for t in range(1, V+1): # goal
                min_cost[s][t] = min(min_cost[s][t], min_cost[s][w] + min_cost[w][t])
    return min_cost


def main():
    # stdin
    n, m, l = map(int, sys.stdin.readline().split())
    dist = [[None for _ in range(n+1)]] + [[None] + [INF for _ in range(n)] for _ in range(n)]
    for s in range(1,n+1):
        dist[s][s] = 0
    for _ in range(m):
        u, v, d = map(int, sys.stdin.readline().split())
        dist[u][v], dist[v][u] = min(dist[u][v], d), min(dist[v][u], d)
        # 問題の条件より、２点間の直経路が一つだけとは限らないので複数あった場合に最短を選択する処理

    q = int(sys.stdin.readline().rstrip())
    st = map(int, sys.stdin.read().split())
    st = zip(st, st)



    shortest_dist = warshall_floyd(n, dist)


    filling_times = [[None for _ in range(n+1)]] + [[None] + [INF for _ in range(n)] for _ in range(n)]
    for s in range(1, n+1):
        for t in range(1, n+1):
            if s == t:
                filling_times[s][t] = 0
            elif shortest_dist[s][t] <= l:
                filling_times[s][t] = 1

    min_filling_times = warshall_floyd(n, filling_times)
    for s, t in st:
        # 最初は満タンのため-1
        print(min_filling_times[s][t] - 1 if not min_filling_times[s][t] == INF else -1)


if __name__ == "__main__":
    main()
