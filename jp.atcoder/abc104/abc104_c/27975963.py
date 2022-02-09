import typing


def main() -> typing.NoReturn:
    n, g = map(int, input().split())
    g //= 100
    pc = []
    for _ in range(n):
        p, c = map(int, input().split())
        pc.append((p, c // 100))


    mn = 1 << 60
    for s in range(1 << n):
        cnt = 0
        tot = 0
        j = -1
        for i in range(n):
            if ~s >> i & 1:
                j = max(j, i)
                continue
            p, c = pc[i]
            cnt += p
            tot += (i + 1) * p
            tot += c

        if tot >= g:
            mn = min(mn, cnt)
            continue
        if j == -1: continue
        q = max(0, (g - tot + j) // (j + 1))
        p, c = pc[j]
        if q >= p: continue
        cnt += q
        mn = min(mn, cnt)
    print(mn)

main()
