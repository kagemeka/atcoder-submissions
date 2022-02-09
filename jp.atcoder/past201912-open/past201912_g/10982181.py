import sys
from itertools import product, combinations

n = int(sys.stdin.readline().rstrip())
happiness = []

for i in range(n):
    happiness.append([None] * (i+1) + [int(x) for x in sys.stdin.readline().split()])

def main():
    option = range(3)
    res = -float('inf')
    for p in product(option, repeat=n):
        tot = 0
        group = [[] for _ in range(3)]
        for i in range(n):
            group[p[i]].append(i)

        for g in group:
            for x, y in combinations(g, 2):
                tot += happiness[x][y]
        res = max(res, tot)

    return res

if __name__ == "__main__":
    ans = main()
    print(ans)
