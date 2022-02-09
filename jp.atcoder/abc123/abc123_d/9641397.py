import sys
from heapq import heappush, heappop

x, y, z, K = map(int, sys.stdin.readline().split())
a, b, c = (sorted(map(int, sys.stdin.readline().split()), reverse=True) for _ in range(3))

def main():
    cand = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
    added = set([(0, 0, 0)])
    for _ in range(K):
        s, i, j, k = heappop(cand)
        yield -s
        if i + 1 < x and not (i+1, j, k) in added:
            heappush(cand, (s + a[i] - a[i+1], i+1, j, k))
            added.add((i+1, j, k))
        if j + 1 < y and not (i, j+1, k) in added:
            heappush(cand, (s + b[j] - b[j+1], i, j+1, k))
            added.add((i, j+1, k))
        if k + 1 < z and not (i, j, k+1) in added:
            heappush(cand, (s + c[k] - c[k+1], i, j, k+1))
            added.add((i, j, k+1))

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
