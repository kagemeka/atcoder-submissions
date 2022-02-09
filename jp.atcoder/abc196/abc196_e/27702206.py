import typing


def main() -> typing.NoReturn:
    n = int(input())
    at = [map(int, input().split()) for _ in range(n)]
    q = int(input())
    x = list(map(int, input().split()))
    sort_idx = sorted(range(q), key=lambda i: x[i])
    x = [x[i] for i in sort_idx]

    inf = 1 << 50
    add = 0
    l, r = -1, q
    l_val = -inf
    r_val = inf
    for a, t in at:
        if t == 1:
            add += a
            l_val += a
            r_val += a
        elif t == 2:
            l_val = max(l_val, a)
            lo, hi = -1, q
            while hi - lo > 1:
                i = (lo + hi) // 2
                v = l_val if i <= l else x[i] + add if i < r else r_val
                if v <= l_val: lo = i
                else: hi = i
            assert lo >= l
            l = lo
            if r <= l: r = l + 1
        else:
            r_val = min(r_val, a)
            lo, hi = -1, q
            while hi - lo > 1:
                i = (lo + hi) // 2
                v = l_val if i <= l else x[i] + add if i < r else r_val
                if v >= r_val: hi = i
                else: lo = i
            assert hi <= r
            r = hi
            if r <= l: l = r - 1

    assert l < r
    # assert l_val <= r_val
    for i in range(q):
        if i <= l: x[i] = l_val
        elif i < r: x[i] += add
        else: x[i] = r_val

    assert all(x[i] <= x[i + 1] for i in range(q - 1))
    res = [0] * q
    for i in range(q):
        res[sort_idx[i]] = x[i]
    print(*res, sep='\n')


main()
