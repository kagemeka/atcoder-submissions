import typing


def main() -> typing.NoReturn:
    m, k = map(int, input().split())
    if k >= 1 << m or m == k == 1:
        print(-1)
        return
    if m == 1:
        print(0, 0, 1, 1)
        return

    a = list(range(1 << m))
    a = a + [k] + a[::-1] + [k]
    print(*a)

main()
