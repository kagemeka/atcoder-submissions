import typing


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    que = [(0, 0)]
    inf = 1 << 60
    dist = [[inf] * w for _ in range(h)]
    dist[0][0] = 0
    dyx = [(1, 0), (0, 1)]

    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w


    for y, x in que:
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not on_grid(ny, nx): continue
            if grid[ny][nx] == '#': continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))

    mx = 0
    for i in range(h):
        for j in range(w):
            if dist[i][j] == inf: continue
            mx = max(mx, dist[i][j])
    print(mx + 1)




main()
