import typing


def main() -> typing.NoReturn:
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy.sort(key=lambda x: x[0])

    mn_x = mx_x = xy[0][0]
    mn_y = mx_y = xy[0][1]
    mx = 0
    for x, y in xy[1:]:
        mx = max(mx, abs(x - mn_x) + abs(y - mn_y), abs(x - mx_x) + abs(y - mx_y))
        if x - mn_x < mn_y - y:
            mn_x, mn_y = x, y
        if x - mx_x < y - mx_y:
            mx_x, mx_y = x, y
    print(mx)

main()
