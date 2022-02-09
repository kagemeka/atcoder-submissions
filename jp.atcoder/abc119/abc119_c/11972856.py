import sys
from itertools import product

n, *abc = map(int, sys.stdin.readline().split())
*l, = map(int, sys.stdin.read().split())

def main():
    cand = []
    for p in product([0, 1, 2, 3], repeat=n):
        group = [[] for _ in range(4)]
        for i in range(n):
            group[p[i]].append(l[i])
        cost = 0
        for i in range(1, 4):
            if not group[i]:
                break
            cost += 10 * (len(group[i]) - 1)
            group[i] = sum(group[i])
        else:
            group = group[1:]
            for i in range(3):
                cost += abs(abc[i] - group[i])
            cand.append(cost)

    print(min(cand))

if __name__ ==  '__main__':
    main()
