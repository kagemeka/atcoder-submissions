import typing
import sys

def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    que = []
    added = set()
    a = list(map(int, sys.stdin.read().split()))
    for x in a[::-1]:
        if x in added: continue
        que.append(x)
        added.add(x)
    for x in range(1, n + 1):
        if x in added: continue
        que.append(x)
        added.add(x)
    print(*que, sep='\n')

main()
