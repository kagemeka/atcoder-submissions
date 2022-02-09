import typing
import sys
import bisect

def main() -> typing.NoReturn:
    # greedy
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    s = a.copy()
    for i in range(n - 1):
        s[i + 1] += s[i]

    for i in range(n - k, n - 1):
        # compare s[i], a[i + 1]
        # i - (n - k) + 1
        c = s[i] // (i - (n - k) + 1)
        if c < a[i + 1]:
            print(c)
            return

    print(s[-1] // k)





main()
