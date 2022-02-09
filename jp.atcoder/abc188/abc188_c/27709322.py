import typing


def argmax(a: typing.List[int]) -> int:
    n = len(a)
    assert n > 0
    i, x = 0, a[0]
    for j in range(n):
        if a[j] <= x: continue
        i, x = j, a[j]
    return i


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    m = 1 << n
    i = argmax(a[:m // 2])
    j = argmax(a[m // 2:]) + m // 2
    print((i if a[i] < a[j] else j) + 1)

main()
