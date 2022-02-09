import sys
from heapq import heappush, heappop

n, m, *ab = map(int, sys.stdin.read().split())
ab = sorted(zip(*[iter(ab)] * 2))

def main():
    res = [0] * m
    hq = []
    i = 0
    for j in range(1, m+1):
        while i < n:
            a, b = ab[i]
            if a <= j:
                heappush(hq, -b)
                i += 1
            else:
                break
        if not hq:
            continue
        res[-j] = -heappop(hq)

    return sum(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
