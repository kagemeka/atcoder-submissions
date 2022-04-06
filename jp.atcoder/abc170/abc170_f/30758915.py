import typing
import collections


def main() -> None:
    h, w, k = map(int, input().split())
    y0, x0, y1, x1 = map(lambda x: int(x) - 1, input().split())
    board = [input() for _ in range(h)]

    def on_board(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w and board[y][x] == "."

    inf = 1 << 60
    dist = [[[(inf, 0)] * 5 for _ in range(w)] for _ in range(h)]
    dist[y0][x0][4] = (0, 0)
    dq: typing.Deque[typing.TUple[int, int, int]] = collections.deque()
    dq.append((y0, x0, 4))

    dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while dq:
        y, x, direction_into = dq.popleft()
        for direction_to in range(4):
            dy, dx = dyx[direction_to]
            ny = y + dy
            nx = x + dx

            if not on_board(ny, nx):
                continue
            prev_dist, prev_stroke = dist[y][x][direction_into]
            next_stroke = 1 + (direction_to == direction_into) * prev_stroke
            weight = 0 if direction_to == direction_into else 1
            if next_stroke > k:
                assert weight == 0
                weight += 1
                next_stroke = 1
            next_dist = prev_dist + weight
            if (next_dist, next_stroke) >= dist[ny][nx][direction_to]:
                continue
            dist[ny][nx][direction_to] = (next_dist, next_stroke)

            if weight == 1:
                dq.append((ny, nx, direction_to))
            else:
                dq.appendleft((ny, nx, direction_to))

    min_dist = inf
    for d, _ in dist[y1][x1]:
        min_dist = min(min_dist, d)
    print(-1 if min_dist == inf else min_dist)


if __name__ == "__main__":
    main()
