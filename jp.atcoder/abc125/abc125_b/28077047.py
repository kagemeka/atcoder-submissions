import typing

def main() -> typing.NoReturn:
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    s = 0
    for i in range(n):
        x = v[i] - c[i]
        if x > 0: s += x
    print(s)

main()
