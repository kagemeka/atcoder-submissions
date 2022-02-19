import sys
from collections import Counter
from heapq import heappop, heappush

n, t, *a = map(int, sys.stdin.read().split())


def main():
    cand = []
    hq = [a[0]]
    for x in a[1:]:
        y = heappop(hq)
        cand.append(x - y)
        heappush(hq, x)
        heappush(hq, y)
    c = Counter(cand)
    ans = c[max(c.keys())]
    print(ans)


if __name__ == "__main__":
    main()
