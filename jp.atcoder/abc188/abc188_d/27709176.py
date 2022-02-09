import typing


def compress_array(
    a: typing.List[int],
) -> typing.Tuple[(typing.List[int], ) * 2]:
    import bisect
    v = sorted(set(a))
    return [bisect.bisect_left(v, x) for x in a], v



def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(n)]

    days = []
    for a, b, _ in abc:
        days.append(a)
        days.append(b + 1)


    days = sorted(set(days))

    m = len(days)
    import bisect
    s = [0] * m
    for a, b, c in abc:
        a = bisect.bisect_left(days, a)
        b = bisect.bisect_left(days, b + 1)
        s[a] += c
        s[b] -= c

    for i in range(m - 1):
        s[i + 1] += s[i]


    tot = 0
    for i in range(m - 1):
        tot += (days[i + 1] - days[i]) * min(k, s[i])
    print(tot)

main()
