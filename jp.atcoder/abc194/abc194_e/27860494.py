import typing


def main() -> typing.NoReturn:
    n, m =  map(int, input().split())
    a = list(map(int, input().split()))
    prev = [-1] * n
    for i in range(n):
        if i - prev[a[i]] > m:
            print(a[i])
            return
        prev[a[i]] = i
    for x in range(n):
        if n - prev[x] > m:
            print(x)
            return
    print(n)

main()
