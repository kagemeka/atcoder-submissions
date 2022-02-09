import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [1 << i for i in range(n)]
    for a, b in ab:
        g[a] |= 1 << b
        g[b] |= 1 << a


    inf = 1 << 60
    cnt = [inf] * (1 << n)
    cnt[0] = 0
    for i in range(n):
        cnt[1 << i] = 1

    rel = [0] * (1 << n)
    for i in range(n):
        rel[1 << i] = g[i]
    for s in range(1 << n):
        t = s
        while t > 0:
            t = (t - 1) & s
            u = s & ~t
            if cnt[t] >= 2 or cnt[u] >= 2:
                cnt[s] = min(cnt[s], cnt[t] + cnt[u])
                continue
            if rel[t] & rel[u] & s == s:
                cnt[s] = 1
                rel[s] = rel[t] & rel[u]
            else:
                cnt[s] = min(cnt[s], 2)
    print(cnt[-1])

main()
