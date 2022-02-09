import typing


def main() -> typing.NoReturn:
    h, w, n = map(int, input().split())
    rca = []
    for i in range(n):
        r, c, a = map(int, input().split())
        r -= 1
        c -= 1
        rca.append((r, c, a, i))

    rca.sort(key=lambda x: -x[2])

    r_max0 = [0] * h
    r_max1 = [0] * h
    c_max0 = [0] * w
    c_max1 = [0] * w

    b = 1 << 60

    res = [0] * n
    r_st = []
    c_st = []
    for r, c, a, i in rca:
        if a != b:
            for x in r_st:
                r_max0[x] = r_max1[x]
            for x in c_st:
                c_max0[x] = c_max1[x]
            r_st, c_st = [], []
        mx = max(r_max0[r], c_max0[c]) + 1
        r_max1[r] = max(r_max1[r], mx)
        c_max1[c] = max(c_max1[c], mx)
        res[i] = mx - 1
        r_st.append(r)
        c_st.append(c)
        b = a
    print(*res, sep='\n')

main()
