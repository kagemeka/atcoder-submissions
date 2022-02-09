import typing


def main() -> typing.NoReturn:
    n, m, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    for i in range(n):
        a[i + 1] += a[i]
    for i in range(m):
        b[i + 1] += b[i]

    ptr = m
    mx = 0
    for i in range(n + 1):
        while ptr >= 0 and a[i] + b[ptr] > k:
            ptr -= 1
        if ptr == -1: break
        mx = max(mx, i + ptr)
    print(mx)

main()
