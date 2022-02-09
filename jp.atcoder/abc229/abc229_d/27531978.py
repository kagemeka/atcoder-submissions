import typing
import bisect


def main() -> typing.NoReturn:
    s = input()
    k = int(input())
    n = len(s)
    a = [int(x == '.') for x in s]
    for i in range(n - 1):
        a[i + 1] += a[i]

    mx = 0
    for i in range(n):
        r = k
        if s[i] == '.': r -= 1
        if r < 0: continue
        mx = max(mx, bisect.bisect_right(a, a[i] + r) - i)
    print(mx)



main()
