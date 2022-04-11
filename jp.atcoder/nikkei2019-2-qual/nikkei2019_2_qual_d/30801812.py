import heapq

def main() -> None:
    # greedy
    # dp
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        l, r, c = map(int, input().split())
        l -= 1
        r -= 1
        g[l].append((r, c))

    inf = 1 << 60
    dist = [inf] * n
    dist[0] = 0

    hq = [(0, 0)]
    for i in range(n):
        while hq and hq[0][1] < i:
            heapq.heappop(hq)
        if not hq:
            print(-1)
            return
        prev_cost, _ = hq[0]
        dist[i] = prev_cost
        for r, c in g[i]:
            next_cost = prev_cost + c
            heapq.heappush(hq, (next_cost, r))
    print(dist[-1])


if __name__ == "__main__":
    main()
