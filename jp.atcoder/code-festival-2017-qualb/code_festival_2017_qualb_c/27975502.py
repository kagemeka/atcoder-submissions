import typing



def is_bipartite(g: typing.List[typing.List[int]]) -> bool:
    n = len(g)
    assert n >= 1
    label = [-1] * n
    label[0] = 0
    que = [0]
    for u in que:
        for v in g[u]:
            if label[v] == label[u]: return False
            if label[v] != -1: continue
            label[v] = label[u] ^ 1
            que.append(v)
    assert all(l != -1 for l in label)
    return True

def label_bipartite(g: typing.List[typing.List[int]]) -> bool:
    assert is_bipartite(g)
    n = len(g)
    label = [-1] * n
    label[0] = 0
    que = [0]
    for u in que:
        for v in g[u]:
            if label[v] != -1: continue
            label[v] = label[u] ^ 1
            que.append(v)
    return label



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [[] for _ in range(n)]
    for a, b in ab:
        g[a].append(b)
        g[b].append(a)
    if is_bipartite(g):
        label = label_bipartite(g)
        c = label.count(1)
        print(c * (n - c) - m)
    else:
        print(n * (n - 1) // 2 - m)

main()
