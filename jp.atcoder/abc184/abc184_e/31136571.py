import collections


def main() -> None:
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    # bfs
    # if we visit a cell once, remove the cell from cell set to visit.

    cell_list = collections.defaultdict(list)
    for i in range(h):
        for j in range(w):
            if "a" <= a[i][j] <= "z":
                cell_list[a[i][j]].append((i, j))
            elif a[i][j] == "S":
                sy, sx = i, j
            elif a[i][j] == "G":
                gy, gx = i, j

    teleport_used = collections.defaultdict(bool)  # a-z

    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w

    INF = 1 << 60
    dist = [[INF] * w for _ in range(h)]
    dist[sy][sx] = 0
    dyx = ((-1, 0), (0, -1), (0, 1), (1, 0))
    que = [(sy, sx)]
    for y, x in que:
        d = dist[y][x] + 1
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not on_grid(ny, nx) or a[ny][nx] == "#":
                continue
            if d >= dist[ny][nx]:
                continue
            dist[ny][nx] = d
            que.append((ny, nx))
        if teleport_used[a[y][x]]:
            continue
        for ny, nx in cell_list[a[y][x]]:
            if d >= dist[ny][nx]:
                continue
            dist[ny][nx] = d
            que.append((ny, nx))

        teleport_used[a[y][x]] = True
    res = dist[gy][gx]
    print(-1 if res == INF else res)


if __name__ == "__main__":
    main()
