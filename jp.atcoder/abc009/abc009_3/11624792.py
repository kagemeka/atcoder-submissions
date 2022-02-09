import sys
from heapq import heappush, heappop

n, k = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())

def main(k):
    swapped = [False] * n

    for i in range(n - 1):
        r = k - (swapped[i] ^ 1)
        q = []
        for j in range(i + 1, n):
            if s[j] >= s[i]: continue
            cost = swapped[j] ^ 1
            if r - cost < 0: continue
            heappush(q, (s[j], cost - r, -j))
        if not q: continue
        char, k, j = heappop(q)
        k *= -1; j *= -1
        s[i], s[j] = s[j], s[i]
        swapped[i] = swapped[j] = True

    print(''.join(s))

if __name__ ==  '__main__':
    main(k)
