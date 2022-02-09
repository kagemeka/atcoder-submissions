import typing


def main() -> typing.NoReturn:
    n = int(input())

    # r = 0, 1, 2
    # if r == 0, it's not needed to delete any digit.
    # if r == 1, if there is at least one element r == 1, answer is 1 other wise 2
    # if r == 2, if there is at least one element r == 2, answer is 1 other wise 2

    cnt = [0] * 3
    s = 0
    l = 0
    while n:
        n, r = divmod(n, 10)
        r %= 3
        cnt[r] += 1
        s = (s + r) % 3
        l += 1

    if s == 0:
        ans = 0
    elif s == 1:
        if cnt[1] >= 1:
            ans = 1
        else:
            ans = 2
    else:
        if cnt[2] >= 1:
            ans = 1
        else:
            ans = 2
    print(ans if ans < l else -1)

main()
