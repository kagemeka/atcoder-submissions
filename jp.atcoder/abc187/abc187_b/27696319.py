import typing


def main() -> typing.NoReturn:
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    cnt = 0

    def is_ok(i: int, j: int) -> bool:
        xi, yi = xy[i]
        xj, yj = xy[j]
        dx = xj - xi
        dy = yj - yi
        return -dx <= dy and dy <= dx

    xy.sort()
    for i in range(n - 1):
        for j in range(i + 1, n):
            cnt += is_ok(i, j)

    print(cnt)

main()
