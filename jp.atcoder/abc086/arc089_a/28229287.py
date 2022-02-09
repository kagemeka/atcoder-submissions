import typing


def main() -> typing.NoReturn:
    n = int(input())
    txy = [tuple(map(int, input().split())) for _ in range(n)]
    txy = [(0, 0, 0)] + txy

    for i in range(n):
        ti, xi, yi = txy[i]
        tj, xj, yj = txy[i + 1]
        dt = tj - ti
        d = abs(xj - xi) + abs(yj - yi)
        if d <= dt and (dt - d) % 2 == 0:
            continue
        print('No')
        return
    print('Yes')

main()
