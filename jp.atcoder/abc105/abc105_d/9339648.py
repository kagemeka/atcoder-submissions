import sys
from collections import defaultdict
from itertools import accumulate

n, m, *a = map(int, sys.stdin.read().split())


def main():
    cumsum = list(accumulate(a))
    c = defaultdict(int)
    for s in cumsum:
        c[s % m] += 1

    res = 0
    res += c[0]
    for v in c.values():
        res += (1 + v - 1) * (v - 1) // 2

    return res


if __name__ == "__main__":
    ans = main()
    print(ans)
