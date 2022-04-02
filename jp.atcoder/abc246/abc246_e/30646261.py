import collections


def main() -> None:
    n = int(input())
    ay, ax = map(int, input().split())
    by, bx = map(int, input().split())
    ay -= 1
    ax -= 1
    by -= 1
    bx -= 1
    s = [input() for _ in range(n)]
    # shortest path
    # manage node and direction
    # 01BFS

    dyx = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    dyx = list(enumerate(dyx))

    def on_board(y: int, x: int) -> bool:
        return 0 <= y < n and 0 <= x < n

    dq = collections.deque()
    inf = 1 << 60
    dist = [[[inf] * 5 for _ in range(n)] for _ in range(n)]
    dist[ay][ax][4] = 0
    dq.append((ay, ax, 4))  # y, x, direction

    while dq:
        y, x, direction = dq.popleft()
        for direct, (dy, dx) in dyx:
            ny, nx = y + dy, x + dx
            if not on_board(ny, nx):
                continue
            if s[ny][nx] == "#":
                continue
            weight = 0 if direct == direction else 1
            # for j in range(4):
            d = dist[y][x][direction] + weight
            if d >= dist[ny][nx][direct]:
                continue
            dist[ny][nx][direct] = d
            if weight == 0:
                dq.appendleft((ny, nx, direct))
            else:
                dq.append((ny, nx, direct))
    # for d in dist:
    #     print(d)

    # print(ay, ax, by, bx)
    res = min(dist[by][bx])
    print(res if res != inf else -1)
    # print(min(dist[by][bx]))
    # print(dist)
    # for d in dist:
    #     print(d)
    # print(dist[2])


if __name__ == "__main__":
    main()
