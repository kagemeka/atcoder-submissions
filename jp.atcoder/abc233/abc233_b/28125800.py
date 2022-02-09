import typing

def main() -> typing.NoReturn:
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    s = list(input())
    s[l:r + 1] = s[l:r + 1][::-1]
    print(''.join(s))

main()
