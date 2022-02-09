import typing


def count_toposort(
    graph: typing.List[typing.List[int]],
    mod: typing.Optional[int] = None,
) -> int:
    n = len(graph)
    before = [0] * n
    for u in range(n):
        for v in graph[u]:
            before[v] |= 1 << u
    cnt = [0] * (1 << n)
    cnt[0] = 1
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            t = s & ~(1 << i)
            if before[i] & ~t != 0:
                continue
            cnt[s] += cnt[t]
            if mod is not None:
                cnt[s] %= mod
    return cnt[-1]


def main() -> None:
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
    print(count_toposort(graph))

main()
