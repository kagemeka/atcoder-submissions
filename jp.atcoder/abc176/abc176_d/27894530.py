import typing



def zero_one_bfs(
    g: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
) -> typing.List[int]:
    import collections
    n = len(g)
    inf = 1 << 60
    dist = [inf] * n
    dist[src] = 0
    que = collections.deque()
    que.append(src)
    while que:
        u = que.popleft()
        for v, w in g[u]:
            if dist[v] <= dist[u] + w: continue
            dist[v] = dist[u] + w
            if w == 0:
                que.appendleft(v)
            else:
                que.append(v)
    return dist



def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())

    grid = [input() for _ in range(h)]

    n = h * w
    g = [[] for _ in range(n)]

    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w


    dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#': continue
            for dy, dx in dyx:
                ni = i + dy
                nj = j + dx
                if not on_grid(ni, nj): continue
                if grid[ni][nj] == '#': continue
                g[i * w + j].append((ni * w + nj, 0))
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    ni = i + dy
                    nj = j + dx
                    if not on_grid(ni, nj): continue
                    if grid[ni][nj] == '#': continue
                    g[i * w + j].append((ni * w + nj, 1))
    dist = zero_one_bfs(g, sy * w + sx)
    inf = 1 << 60
    d = dist[gy * w + gx]
    print(-1 if d == inf else d)


main()
