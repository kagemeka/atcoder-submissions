import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())
    v = list(map(int, input().split()))
    a = collections.Counter(v[::2]).items()
    b = collections.Counter(v[1::2]).items()
    a = sorted(a, key=lambda x: -x[1])
    b = sorted(b, key=lambda x: -x[1])
    if a[0][0] != b[0][0]:
        print(n - a[0][1] - b[0][1])
        return
    if len(a) == 1 and len(b) == 1:
        print(n // 2)
        return

    if len(a) == 1:
        print(n - a[0][1] - b[1][1])
    elif len(b) == 1:
        print(n - a[1][1] - b[0][1])
    else:
        print(n - max(a[0][1] + b[1][0], a[1][1] + b[0][1]))

main()
