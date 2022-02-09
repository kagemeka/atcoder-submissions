# 2019-11-24 20:59:47(JST)
import sys
# import numpy as np
import collections
import copy

def main():
    n = int(sys.stdin.readline().rstrip())
    ab = map(int, sys.stdin.read().split())
    ab = zip(ab, ab)
    A = copy.deepcopy(ab)
    graph = collections.defaultdict(list)

    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)

    needed_colors = max(len(graph[i]) for i in range(1, n+1))

    res = collections.defaultdict(dict)

    number = 1
    for a, v in graph.items():
        for b in v:
            if res[a]:
                values = res[a].values()
                while number in values:
                    number += 1
                    if number == needed_colors + 1:
                        number = 1
                continue
            res[a][b] = number
            res[b][a] = number
            number += 1
            if number == needed_colors + 1:
                        number = 1

    print(needed_colors)

    for a, b in A:
        print(res[a][b])


if __name__ == '__main__':
    main()
