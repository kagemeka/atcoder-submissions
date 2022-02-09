import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    b = [-1] * n
    for i in range(n, 0, -1):
        s = 0
        for j in range(i * 2, n + 1, i):
            s ^= b[j - 1]
        b[i - 1] = s ^ a[i - 1]

    s = sum(b)
    print(s)
    if not s: return
    print(*[i + 1 for i in range(n) if b[i]])
main()
