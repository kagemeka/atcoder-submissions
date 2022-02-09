import sys
from itertools import product

inf = float('inf')

n, *target = map(int, sys.stdin.readline().split())
target = [None] + target
*l,  = map(int, sys.stdin.read().split())

def main():
    costs = []
    for p in product(range(4), repeat=n):
        tmp = [[] for _ in range(4)]
        p = list(p)
        for i in range(n):
            tmp[p[i]].append(l[i])

        cost = [0] * 4
        for i in range(1, 4):
            if not tmp[i]:
                break
            cost[i] += 10 * (len(tmp[i]) - 1)
            cost[i] += abs(target[i] - sum(tmp[i]))
        else:
            costs.append(sum(cost))

    return min(costs)

if __name__ == '__main__':
    ans = main()
    print(ans)
