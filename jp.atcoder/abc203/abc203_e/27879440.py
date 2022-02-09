import typing
import bisect
def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    xy = [tuple(map(int, input().split())) for _ in range(m)]
    a = sorted(set([x for x, y in xy]))
    xy = [(bisect.bisect_left(a, x) + 1, y) for x, y in xy]
    y_list = [[] for _ in range(len(a) + 1)]
    for x, y in xy:
        y_list[bisect.bisect_left(a, x) + 1].append(y)

    s = set()
    s.add(n)
    for ys in y_list[1:]:
        to_add = set()
        to_remove = set()
        for y in ys:
            if y - 1 in s or y + 1 in s:
                to_add.add(y)
            else:
                to_remove.add(y)
        s |= to_add
        s -= to_remove
    print(len(s))


main()
