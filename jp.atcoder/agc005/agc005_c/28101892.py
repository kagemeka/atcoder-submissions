import typing


def main() -> typing.NoReturn:
    # mathematical induction
    # if max distance is d_mx,
    # the count of i such that a_i = d_mx is more than or equal to 2
    # and a_i = d_mx - 1 is also more than or equal to 2, and less than or equal to the count of i (a_i = d_mx)
    # except for tha min value (it's more than or equal to 1)
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for x in a:
        cnt[x] += 1

    if n > 2 and cnt[1] >= 2:
        print('Impossible')
        return
    que = [(d, cnt[d]) for d in range(n - 1, 0, -1) if cnt[d]]

    m = len(que)
    inf = 1 << 60
    c_mx = inf
    d_mx = inf
    for i, (d, c) in enumerate(que):
        ok = True
        if i == 0:
            if c <= 1: ok = False
        if i > 0 and d != d_mx - 1:
            ok = False
        if c > c_mx:
            ok = False
        if i < m - 1 and c < 2:
            ok = False
        if not ok:
            print('Impossible')
            return
        d_mx, c_mx = d, c
    print('Possible')

main()
