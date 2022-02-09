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
        g[a].append(b)
        g[b].append(a)
    s = input()
    k = s.index('g') + 1
    ptn = re.compile(r'^[^\d]*(\d+)[^\d]*$')
    m = re.match(ptn, s)
    s = int(m.groups()[0]) - 1

    a = [s]
    for _ in range(k):
        a = list(set(y for x in a for y in g[x]))
    print(len(a))

main()
