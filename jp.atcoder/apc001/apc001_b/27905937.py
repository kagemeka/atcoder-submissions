import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    neg = 0
    for i in range(n):
        neg += max(0, a[i] - b[i])
    print('Yes' if sum(b) - sum(a) >= neg else 'No')

main()
