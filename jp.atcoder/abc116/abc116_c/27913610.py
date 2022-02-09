import typing


def main() -> typing.NoReturn:
    n = int(input())
    h = list(map(int, input().split()))

    cnt = 0
    while any(x > 0 for x in h):
        flag = False
        for i in range(n):
            if h[i] == 0:
                flag = False
                continue
            h[i] -= 1
            if not flag:
                cnt += 1
            flag = True
    print(cnt)

main()
