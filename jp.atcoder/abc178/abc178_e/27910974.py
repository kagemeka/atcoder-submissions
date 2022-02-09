import typing


def main() -> typing.NoReturn:
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    a = [x - y for x, y in xy]
    b = [x + y for x, y in xy]
    mx = max(max(a) - min(a), max(b) - min(b))
    print(mx)

main()
