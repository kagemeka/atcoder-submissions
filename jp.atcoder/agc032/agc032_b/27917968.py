import typing

def main() -> typing.NoReturn:
    n = int(input())

    edges = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            edges.add((i, j))

    if n & 1:
        for i in range(n // 2):
            edges.remove((i, n - 2 - i))
    else:
        for i in range(n // 2):
            edges.remove((i, n - 1 - i))

    print(len(edges))
    for i, j in edges:
        print(i + 1, j + 1)


main()
