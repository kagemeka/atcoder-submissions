import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())
    d = list(map(int, input().split()))
    m = int(input())
    t = list(map(int, input().split()))
    cd = collections.Counter(d)
    ct = collections.Counter(t)
    for k, c in ct.items():
        if cd[k] >= c: continue
        print('NO')
        return
    print('YES')

main()
