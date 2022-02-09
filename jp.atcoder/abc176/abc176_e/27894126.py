import typing


def main() -> typing.NoReturn:
    h, w, m = map(int, input().split())
    yx = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    y_list = [set() for _ in range(w)]
    x_list = [set() for _ in range(h)]
    for y, x in yx:
        y_list[x].add(y)
        x_list[y].add(x)

    x_mx_cnt = max([len(ls) for ls in x_list])
    y_cand = [y for y in range(h) if len(x_list[y]) == x_mx_cnt]
    y_mx_cnt = max([len(ls) for ls in y_list])
    x_cand = [x for x in range(w) if len(y_list[x]) == y_mx_cnt]

    s = x_mx_cnt + y_mx_cnt
    x_cand = set(x_cand)
    for y in y_cand:
        if len(x_cand - x_list[y]) == 0:
            continue
        print(s)
        return
    print(s - 1)


main()
