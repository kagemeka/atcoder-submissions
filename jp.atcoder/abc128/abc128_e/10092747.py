import sys
from heapq import heappush, heappop

n, q = map(int, sys.stdin.readline().split())
stx = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
*d, = map(int, sys.stdin.read().split())

def main():
    queue = []
    for s, t, x in stx:
        queue.append((s-x, 1, x))
        queue.append((t-x, 0, x))

    for i in range(q):
        queue.append((d[i], 2, i))

    queue.sort()

    res = [None] * q
    hq = []
    running = set()

    for t, f, x in queue:
        if f == 1:
            heappush(hq, x)
            running.add(x)
        elif f == 0:
            running -= set([x])
        elif f == 2:
            i = x
            while hq:
                if not hq[0] in running:
                    heappop(hq)
                    continue
                res[i] = hq[0]
                break
            else:
                res[i] = -1
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
