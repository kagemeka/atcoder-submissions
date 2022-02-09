import typing


def main() -> typing.NoReturn:
    n = int(input())
    at = [map(int, input().split()) for _ in range(n)]
    q = int(input())
    x = list(map(int, input().split()))
    sort_idx = sorted(range(q), key=lambda i: x[i])
    x = [x[i] for i in sort_idx]

    add = 0
    l, r = 0, q - 1
    l_val = x[l]
    r_val = x[r]
    for a, t in at:
        if t == 1:
            add += a
            l_val += a
            r_val += a
        elif t == 2:
            l_val = max(l_val, a)
            while l + 1 < n and x[l + 1] + add <= l_val: l += 1
            if r < l: r = l
        else:
            r_val = min(r_val, a)
            while r - 1 >= 0 and x[r - 1] + add >= r_val: r -= 1
            if l > r: l = r

    for i in range(q):
        if i <= l: x[i] = l_val
        elif i < r: x[i] += add
        else: x[i] = r_val

    res = [0] * q
    for i in range(q):
        res[sort_idx[i]] = x[i]
    print(*res, sep='\n')


main()
