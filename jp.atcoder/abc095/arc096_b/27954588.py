import typing


def main() -> typing.NoReturn:
    n, c = map(int, input().split())
    xv = [tuple(map(int, input().split())) for _ in range(n)]
    inf = 1 << 60
    vl = [-inf] * (n + 1)
    vl[0] = 0
    for i in range(n):
        x, v = xv[i]
        vl[i + 1] = vl[i] + v
    for i in range(n):
        x, v = xv[i]
        vl[i + 1] -= x

    vr = [-inf] * (n + 1)
    vr[0] = 0
    for i in range(n):
        x, v = xv[-1 - i]
        vr[-i - 1] = vr[-i] + v
    for i in range(n):
        x, v = xv[-1 - i]
        vr[-i - 1] -= c - x

    sl = [-inf] * (n + 1)
    sl[0] = 0
    for i in range(n):
        x, v = xv[i]
        sl[i + 1] = max(sl[i], vl[i + 1] - x)
    sr = [-inf] * (n + 1)
    sr[0] = 0
    for i in range(n):
        x, v = xv[-1 - i]
        sr[-1 - i] = max(sr[-i], vr[-1 - i] - (c - x))

    res = 0
    for i in range(n):
        res = max(res, vl[i + 1] + sr[(i + 2) % (n + 1)])

    for i in range(n, 0, -1):
        res = max(res, vr[i] + sl[i - 1])


    print(res)



main()
