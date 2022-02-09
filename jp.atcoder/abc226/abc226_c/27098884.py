import typing



def main() -> typing.NoReturn:
    n = int(input())
    t = []
    a = []
    # z = []
    for _ in range(n):
        _t, k, *_a, = map(int, input().split())
        t.append(_t)
        a.append(_a)

    tot = 0
    ok = [False] * n
    que = [n - 1]
    tot += t[n - 1]
    ok[n - 1] = True
    for i in que:
        for j in a[i]:
            j -= 1
            if ok[j]: continue
            tot += t[j]
            ok[j] = True
            que.append(j)
    print(tot)


main()
