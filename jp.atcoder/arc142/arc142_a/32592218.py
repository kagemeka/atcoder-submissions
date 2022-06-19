# mypy: ignore-errors


def main() -> None:
    n, k = map(int, input().split())

    # check k is minimum.

    if k % 10 == 0:
        print(0)
        return

    m = int(str(k)[::-1])
    if m < k:
        print(0)
        return

    cnt = 0
    cnt += 1 <= k <= n
    while True:
        k *= 10
        if not 1 <= k <= n:
            break
        cnt += 1

    if m != k:
        cnt += 1 <= m <= n
        while True:
            m *= 10
            if not 1 <= m <= n:
                break
            cnt += 1
    print(cnt)

    # 0, 1, 2


main()
