import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))


    s = t = 0
    r = 0
    cnt = 0
    for l in range(n):
        while r < n and s + a[r] == t ^ a[r]:
            s += a[r]
            t ^= a[r]
            r += 1
        cnt += r - l
        if r == l:
            r += 1
            continue
        s -= a[l]
        t ^= a[l]
    print(cnt)

main()
