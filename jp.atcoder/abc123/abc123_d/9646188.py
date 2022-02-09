import sys
from heapq import heappush, heappop

x, y, z, k = map(int ,sys.stdin.readline().split())
a, b, c = (sorted(map(int, sys.stdin.readline().split())) for _ in range(3))

def main():
    res = []
    for i in range(x):
        for j in range(y):
            heappush(res, -(a[i] + b[j]))

    res2 = []
    for i in range(min(k, x * y)):
        ab = -heappop(res)
        for j in range(z):
            heappush(res2, -(ab + c[j]))

    for i in range(k):
        yield -heappop(res2)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
