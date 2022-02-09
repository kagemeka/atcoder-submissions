import typing


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]


    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w


    def count(i: int, j: int) -> int:
        cnt = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == dx == 0: continue
                y, x = i + dy, j + dx
                if not on_grid(y, x): continue
                cnt += s[y][x] == '#'
        return cnt


    for i in range(h):
        for j in range(w):
            if s[i][j] == '#': continue
            s[i][j] = count(i, j)

    for row in s:
        print(''.join(map(str, row)))


main()
