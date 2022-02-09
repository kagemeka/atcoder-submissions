import typing



def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    # mn, mx
    # after: mn := multiple of a[i], mx := multiple of a[i]
    # before: mn := multiple of a[i], mx := multiple of a[i] + (a[i] - 1)
    # if there is no x (mn <= x <= mx \land x = c*a[i]), impossible.

    mn = mx = 2

    for p in a[::-1]:
        if mx // p * p < mn:
            print(-1)
            return
        mx = mx // p * p + p - 1
        mn = (mn + p - 1) // p * p
    print(mn, mx)

main()
