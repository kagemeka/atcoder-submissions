import typing


def main() -> typing.NoReturn:
    h, w, m = map(int, input().split())
    yx = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    y_cnt = [0] * w
    x_cnt = [0] * h
    for y, x in yx:
        y_cnt[x] += 1
        x_cnt[y] += 1

    x_mx_cnt = max(x_cnt)
    y_mx_cnt = max(y_cnt)
    y_cand = [y for y in range(h) if x_cnt[y] == x_mx_cnt]
    x_cand = [x for x in range(w) if y_cnt[x] == y_mx_cnt]

    s = x_mx_cnt + y_mx_cnt
    if len(y_cand) * len(x_cand) > m:
        print(s)
        return

    yx = set(yx)
    for y in y_cand:
        for x in x_cand:
            if (y, x) in yx: continue
            print(s)
            return
    print(s - 1)


main()
