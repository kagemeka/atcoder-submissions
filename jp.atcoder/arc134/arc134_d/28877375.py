import typing


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    left, right = [], []

    inf = 1 << 60
    mn = inf
    for i in range(n - 1, -1, -1):
        if a[i] > mn:
            continue
        mn = a[i]
        left.append(a[i])
        right.append(a[i + n])
    left.reverse()
    right.reverse()

    prev = left[0]
    mn = right[0]
    m = len(left)
    i = 1
    res = [0]
    while i < m:
        if left[i] != prev:
            break
        if right[i] < mn:
            mn = right[i]
        res.append(i)
        i += 1
    if mn <= prev:
        print(prev, mn)
        return

    flg = True
    for j in range(m - 1):
        if right[j] < right[j + 1]:
            flg = False
            break

    while i < m:
        if left[i] == prev:
            res.append(i)
            i += 1
            continue
        if left[i] > right[0]:
            break
        if not flg and left[j] >= right[0]:
            break

        prev = left[i]
        res.append(i)
        i += 1

    ans = [left[i] for i in res] + [right[i] for i in res]
    print(*ans)


if __name__ == "__main__":
    main()
