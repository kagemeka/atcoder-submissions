import heapq


def main() -> None:
    # suppose arrive node_i at t_i for earliest.
    # and wait there dt.

    # compute dt such that f(dt) = dt + [d_i / (t_i + dt + 1)]
    # achieve the minimum.
    # draw this function.
    # such a dt value can be computed with ternary search.
    # now, let's get down to a simple shortest path problem with dijkstra.

    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append((b, c, d))
        g[b].append((a, c, d))

    inf = 1 << 60
    min_time = [inf] * n
    min_time[0] = 0
    hq = [(0, 0)]

    def take_time(t: int, c: int, d: int) -> int:
        return c + d // (t + 1)

    def take_time_with_dt(dt: int, t: int, c: int, d: int) -> int:
        return dt + take_time(t + dt, c, d)

    def ternary_search_dt(t: int, c: int, d: int) -> int:

        lo, hi = 0, inf
        while hi - lo > 0:
            dt_0 = (lo * 2 + hi) // 3
            dt_1 = (lo + hi * 2) // 3
            t0 = take_time_with_dt(dt_0, t, c, d)
            t1 = take_time_with_dt(dt_1, t, c, d)
            if t0 <= t1:
                hi = dt_1
            else:
                lo = dt_0 + 1
            # print(lo, hi, dt_0, dt_1, t0, t1)
        return lo

    while hq:
        t, u = heapq.heappop(hq)
        if t > min_time[u]:
            continue
        for v, c, d in g[u]:
            dt = ternary_search_dt(t, c, d)
            t_v = t + take_time_with_dt(dt, t, c, d)
            if t_v >= min_time[v]:
                continue
            min_time[v] = t_v
            heapq.heappush(hq, (t_v, v))

    # print(min_time)
    print(min_time[-1] if min_time[-1] != inf else -1)


if __name__ == "__main__":
    main()
