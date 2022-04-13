import heapq


def main() -> None:
    # suppose arrive node_i at t_i for earliest.
    # and wait there dt.

    # compute dt such that f(dt) = dt + d_i // (t_i + dt + 1)
    # achieve the minimum.
    # draw this function.
    # ternary search is wrong.
    # reference: https://youtu.be/ZqFtoX-W1Bk?t=7380
    # consider the border.
    # let g(t) := t - a + d_i // t
    # (t = t_i + dt + 1, t - a = dt)
    # if d / t - d / (t + 1) > 1,
    # then d // t - d // (t + 1) >= 1
    # thus g(t) - g(t + 1) >= 1 - 1 >= 0 # weakly monotonic decreasing.
    # if d / t - d / (t + 1) <= 1,
    # then d // t - d // (t + 1) <= 1,
    # thus g(t) - g(t + 1) <= 1 - 1 <= 0 # weakly monotonic increasing.

    # so we it's fine if we can compute the minimum t
    # satisfying d / t - d / (t + 1) <= 1

    # d <= t(t + 1)
    # if t^2 + t - d = 0,
    # t = (-1 + \sqrt{1 + 4d}) / 2 (because t >= 0)
    # therefore (1 + \sqrt{4d + 1}) / 2 > t >= (-1 + \sqrt{4d + 1}) / 2
    # thus 1 + \sqrt{d} > t > -1/2 + \sqrt{d}
    # so, t = floor[\sqrt{d}] or ceil[\sqrt{d}]

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

    def compute_dt(t: int, c: int, d: int) -> int:
        t_0 = int(d**0.5)
        if t_0 == 0:
            t_0 += 1
        if t_0 * t_0 < d:
            t_1 = t_0 + 1
            if t_1 + d // t_1 < t_0 + d // t_0:
                t_0 = t_1
        return max(0, t_0 - t - 1)

    while hq:
        t, u = heapq.heappop(hq)
        if t > min_time[u]:
            continue
        for v, c, d in g[u]:
            # dt = max(0, int(d**0.5) - t)
            dt = compute_dt(t, c, d)
            t_v = t + dt + take_time(t + dt, c, d)
            if t_v >= min_time[v]:
                continue
            min_time[v] = t_v
            heapq.heappush(hq, (t_v, v))

    # print(min_time)
    print(min_time[-1] if min_time[-1] != inf else -1)


if __name__ == "__main__":
    main()
