import typing

def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = [[] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))[1:]

    que = a[0]
    for i in range(n - 1):
        b = []
        for x in a[i + 1]:
            for y in que:
                b.append(x * y)
        que = b
    print(que.count(k))

main()
