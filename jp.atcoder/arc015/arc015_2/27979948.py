import typing


def main() -> typing.NoReturn:
    n = int(input())
    cnt = [0] * 6
    for _ in range(n):
        mx, mn = map(float, input().split())
        if mx >= 35: cnt[0] += 1
        elif mx >= 30: cnt[1] += 1
        elif mx >= 25: cnt[2] += 1
        if mn >= 25: cnt[3] += 1
        if mn < 0 and mx >= 0: cnt[4] += 1
        if mx < 0: cnt[5] += 1

    print(*cnt)

main()
