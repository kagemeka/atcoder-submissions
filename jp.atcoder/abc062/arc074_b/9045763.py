import sys
from collections import deque
from heapq import *

n, *a = map(int, sys.stdin.read().split())

def main():
    first = a[:n]
    last = a[n*2:]
    cand = deque(a[n:n*2])

    heapify(first)
    for i in range(n):
        last[i] = -last[i]
    heapify(last)

    first_min = heappop(first)
    last_max = -heappop(last)

    for _ in range(n):
        if cand[0] - first_min >= last_max - cand[-1]:
            first_min = heappushpop(first, cand.popleft())
        else:
            last_max = -heappushpop(last, -cand.pop())

    heappush(first, first_min)
    heappush(last, -last_max)

    return sum(first) - (-sum(last))

if __name__ == '__main__':
    ans = main()
    print(ans)
