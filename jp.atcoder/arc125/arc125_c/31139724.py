import bisect


def main() -> None:

    # we can insert only x satisfying x < a_i or a_{i+1} < x
    # between a_i and a_{i+1}
    # we should insert x at next to upper bound position primalily.
    # if upper bound position does not exist,
    # insert it to previous to lower_bound position.
    # inserted values should be sorted in descending order for each section.

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sections = [[] for _ in range(k + 1)]
    for x in sorted(set(range(1, n + 1)) - set(a), reverse=True):
        i = bisect.bisect_left(a, x)
        if i == k:
            sections[k - 1].append(x)
        else:
            sections[i + 1].append(x)

    p = sections[0]
    for i in range(k):
        p.append(a[i])
        p += sections[i + 1]
    print(*p)


if __name__ == "__main__":
    main()
