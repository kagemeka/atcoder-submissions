import typing


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]


    def on_grid(i: int, j: int) -> bool:
        return 0 <= i < h and 0 <= j < w

    def count(i: int, j: int) -> int:
        cnt = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                y, x = i + dy, j + dx
                if not on_grid(y, x): continue
                cnt += grid[y][x] == '#'
        return cnt

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#': continue
            grid[i][j] = str(count(i, j))

    for row in grid:
        print(''.join(row))


main()
