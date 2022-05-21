import collections

import bisect


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    b = list(collections.Counter(a).values())

    origin = sorted(set(b))

    b = [bisect.bisect_left(origin, x) for x in b]
    mx = max(b)
    cc = [0] * (mx + 1)
    for c in b:
        cc[c] += 1

    def choose_3(n):
        return n * (n - 1) * (n - 2) // 6

    def choose_2(n):
        return n * (n - 1) // 2

    tot = 0
    for i in range(mx + 1):
        o = origin[i]
        tot += choose_3(cc[i]) * o**3
        tot += choose_2(cc[i]) * o**2 * (n - cc[i] * o)

    s = [cc[i] * origin[i] for i in range(mx + 1)]
    for i in range(mx):
        s[i + 1] += s[i]

    for i in range(mx):
        oi = origin[i]
        for j in range(i + 1, mx + 1):
            if cc[i] == 0 or cc[j] == 0:
                continue
            oj = origin[j]
            tot += cc[i] * oi * cc[j] * oj * (n - s[j])
    print(tot)


if __name__ == "__main__":
    main()
