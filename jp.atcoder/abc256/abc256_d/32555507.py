# mypy: ignore-errors

import sys

sys.setrecursionlimit(10**6)


def main() -> None:
    # reverse smallest in each cycle

    n = int(input())
    # imos

    k = 1 << 18
    a = [0] * k
    for _ in range(n):
        l, r = map(int, input().split())
        a[l] += 1
        a[r] -= 1

    for i in range(k - 1):
        a[i + 1] += a[i]

    res = []
    i = -1
    while i <= k:
        while i < k and a[i] == 0:
            i += 1
        if i == k:
            break
        l = i
        while i < k - 1 and a[i + 1] > 0:
            i += 1
        i += 1

        res.append((l, i))
    for l, r in res:
        print(l, r)


if __name__ == "__main__":
    main()
