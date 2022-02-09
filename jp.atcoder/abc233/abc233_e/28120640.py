import typing

def main() -> typing.NoReturn:
    x = list(map(int, input()))
    n = len(x)
    a = [0] * n
    a = x.copy()
    for i in range(n - 1):
        a[i + 1] += a[i]
    for i in range(n - 1, 0, -1):
        q, r = divmod(a[i], 10)
        a[i] = r
        a[i - 1] += q
    if a[0] >= 10:
        a = [a[0] // 10] + a
        a[1] %= 10
    print(''.join(map(str, a)))


main()
