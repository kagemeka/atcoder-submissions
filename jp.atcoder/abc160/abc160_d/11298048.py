import sys
from itertools import combinations

n, x, y = map(int, sys.stdin.readline().split())

def main():
    res = [0] * (n + 1)
    for i, j in combinations(range(1, n+1), 2):
        d = min(j - i, abs(i - x) + 1 + abs(j - y))
        res[d] += 1

    for i in range(1, n):
        print(res[i])

if __name__ == "__main__":
    main()
