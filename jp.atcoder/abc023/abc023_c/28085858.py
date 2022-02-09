import typing


def main() -> typing.NoReturn:
    h, w, k = map(int, input().split())
    n = int(input())
    yx = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

    ch = [0] * h
    cw = [0] * w
    for y, x in yx:
        ch[y] += 1
        cw[x] += 1

    cch = [0] * (max(h, k) + 1)
    ccw = [0] * (max(w, k) + 1)
    for c in ch:
        cch[c] += 1
    for c in cw:
        ccw[c] += 1

    s = 0
    for i in range(0, k + 1):
        s += cch[i] * ccw[k - i]

    for y, x in yx:
        c = ch[y] + cw[x] - 1
        s += c == k
        s -= c == k - 1
    print(s)


main()
