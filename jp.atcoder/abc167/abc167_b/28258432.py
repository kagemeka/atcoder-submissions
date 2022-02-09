import typing

def main() -> typing.NoReturn:
    a, b, c, k = map(int, input().split())
    s = 0
    if k <= a:
        print(k)
        return
    s += a
    k -= a
    if k <= b:
        print(s)
        return
    k -= b
    s -= k
    print(s)

main()
