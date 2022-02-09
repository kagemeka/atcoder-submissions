import typing



def main() -> typing.NoReturn:
    n = int(input())
    s = set()
    for _ in range(n):
        l, *a, = map(int, input().split())
        s.add(tuple(a))
    print(len(s))


main()
