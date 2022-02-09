import typing


def main() -> typing.NoReturn:
    h, w = map(int, input().split())

    # brute force
    # maximum of minimum for each square
    # shortest path
    # bfs


    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w


    maze = [input() for _ in range(h)]


    def compute_dists(
        sy: int,
        sx: int,
    ) -> typing.List[typing.List[typing.Optional[int]]]:

        que = [(sy, sx)]
        dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        dist = [[None] * w for _ in range(h)]
        dist[sy][sx] = 0
        for y, x in que:
            for dy, dx in dyx:
                ny = y + dy
                nx = x + dx
                if not on_grid(ny, nx): continue
                if maze[ny][nx] == '#': continue
                dv = dist[y][x] + 1
                if dist[ny][nx] is not None and dv >= dist[ny][nx]: continue
                dist[ny][nx] = dv
                que.append((ny, nx))
        return dist


    mx = 0
    for y in range(h):
        for x in range(w):
            if maze[y][x] == '#': continue
            dists = compute_dists(y, x)
            mx = max(mx, max(max([d for d in dist if d is not None]) for dist in dists))
    print(mx)

main()
