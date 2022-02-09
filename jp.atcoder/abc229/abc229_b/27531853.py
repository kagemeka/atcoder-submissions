import typing



def main() -> typing.NoReturn:
    a, b = input().split()
    n = min(len(a), len(b))
    for i in range(n):
        x = int(a[-i - 1])
        y = int(b[-i - 1])
        if x + y >= 10:
            print('Hard')
            return
    print('Easy')


main()
