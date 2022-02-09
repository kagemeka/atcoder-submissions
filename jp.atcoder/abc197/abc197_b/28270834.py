import typing


def main() -> typing.NoReturn:
    h, w, y, x = map(int, input().split())
    y -= 1
    x -= 1
    s = [input() for _ in range(h)]

    cnt = 0
    for i in range(y, -1, -1):
        if s[i][x] == '.':
            cnt += 1
            continue
        break

    for i in range(y, h):
        if s[i][x] == '.':
            cnt += 1
            continue
        break

    for j in range(x, -1, -1):
        if s[y][j] == '.':
            cnt += 1
            continue
        break

    for j in range(x, w):
        if s[y][j] == '.':
            cnt += 1
            continue
        break

    cnt -= 3
    print(cnt)

main()
