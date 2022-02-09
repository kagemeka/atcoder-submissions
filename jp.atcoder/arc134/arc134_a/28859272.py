import typing


def main() -> None:
    n, l, w = map(int, input().split())
    a = list(map(int, input().split()))

    a = a + [l]
    cnt = (a[0] + w - 1) // w
    for i in range(n):
        d = max(0, a[i + 1] - (a[i] + w))
        cnt += (d + w - 1) // w
    print(cnt)


if __name__ == "__main__":
    main()
