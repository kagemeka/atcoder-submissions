import typing


def main() -> typing.NoReturn:
    n, d, a = map(int, input().split())
    xh = [tuple(map(int, input().split())) for _ in range(n)]
    xh.sort(key=lambda x: x[0])
    x, h = zip(*xh)
    inf = 1 << 60
    x, h = list(x), list(h)
    x.append(inf)
    h.append(0)
    damage = [0] * (n + 1)
    r = 0
    cnt = 0
    for l in range(n):
        while x[r] <= x[l] + 2 * d: r += 1
        h[l] -= damage[l]
        if h[l] >= 0:
            c = (h[l] + a - 1) // a
            cnt += c
            damage[l] += c * a
            damage[r] -= c * a
        damage[l + 1] += damage[l]
    print(cnt)

main()
