import typing
import sys
import re



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[b].append(a)
    s = input()
    ptn = re.compile(r'^[^\d]*(\d+)([^\d]*)$')
    m = re.match(ptn, s)
    s = int(m.groups()[0]) - 1
    k = m.groups()[1].split('"')

    a = [s]
    for w in k:
        b = set(y for x in a for y in g[x])
        if not w: b = set(range(n)) - b
        a = list(b)
    print(len(a))

main()
