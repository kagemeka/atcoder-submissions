import typing

def main() -> typing.NoReturn:
    n = int(input())
    cnt = 0
    for a in map(int, input().split()):
        while a % 2 == 0 or a % 3 == 2:
            cnt += 1
            a -= 1
    print(cnt)

main()
