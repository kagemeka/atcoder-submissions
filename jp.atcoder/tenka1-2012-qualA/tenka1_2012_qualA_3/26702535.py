import typing
import sys
import re



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # a[a].add(b)
        g[b].add(a)
    s = input()
    ptn = re.compile(r'^[^\d]*(\d+)([^\d]*)$')
    m = re.match(ptn, s)
    s = int(m.groups()[0]) - 1
    k = m.groups()[1].split('"')

    a = [s]
    for w in k:
        if w:
            b = set()
            for x in a: b |= g[x]
        else:
            b = set(range(n))
            for x in a: b -= g[x]
        a = list(b)

    print(len(a))

main()
