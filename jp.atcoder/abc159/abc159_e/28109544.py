import typing


def main() -> typing.NoReturn:
    h, w, k = map(int, input().split())

    a = [list(map(int, input())) for _ in range(h)]

    inf = 1 << 60
    mn = inf
    for s in range(1 << (h - 1)):
        b = []
        b.append(0)
        tot = 0
        for i in range(h - 1):
            if ~s >> i & 1: continue
            b.append(i + 1)
        b.append(h)
        m = len(b)
        base = m - 2
        tmp_mn = inf
        tot = 0
        cnt = [0] * (m - 1)
        for x in range(w):
            tmp = [0] * (m - 1)
            for i in range(m - 1):
                l, r = b[i], b[i + 1]
                for y in range(l, r):
                    tmp[i] += a[y][x]
                cnt[i] += tmp[i]
            if all(cnt[i] <= k for i in range(m - 1)): continue
            cnt = tmp
            tot += 1
        tmp_mn = min(tmp_mn, tot)

        tot = 0
        cnt = [0] * (m - 1)
        for x in range(w - 1, -1, -1):
            tmp = [0] * (m - 1)
            for i in range(m - 1):
                l, r = b[i], b[i + 1]
                for y in range(l, r):
                    tmp[i] += a[y][x]
                cnt[i] += tmp[i]
            if all(cnt[i] <= k for i in range(m - 1)): continue
            cnt = tmp
            tot += 1
        tmp_mn = min(tmp_mn, tot)
        mn = min(mn, tmp_mn + base)

    print(mn)

main()
