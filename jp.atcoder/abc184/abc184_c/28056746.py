import typing

def main() -> typing.NoReturn:
    r0, c0 = map(int, input().split())
    r1, c1 = map(int, input().split())

    r, c = abs(r1 - r0), abs(c1 - c0)
    if r == c == 0:
        ans = 0
    elif r == c or r + c <= 3:
        ans = 1
    elif (r + c) % 2 == 0 or r + c <= 6 or abs(r - c) <= 3:
        ans = 2
    else:
        ans = 3
    print(ans)

main()
