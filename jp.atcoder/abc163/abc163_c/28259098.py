import typing

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    cnt = [0] * n
    for x in a:
        cnt[x] += 1
    print(*cnt, sep='\n')

main()
