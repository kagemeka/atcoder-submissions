import typing



class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def find(self, u: int) -> typing.NoReturn:
        d = self.__data
        if d[u] < 0: return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> typing.NoReturn:
        u, v = self.find(u), self.find(v)
        if u == v: return
        d = self.__data
        if d[u] > d[v]: u, v = v, u
        d[u] += d[v]
        d[v] = u



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # at first graph is forest (it may be connected as initial state.)
    # from small cost to large cost (greedy)
    # if two nodes are in same connected component, do not unite.
    # UnionFind, check connectivity

    xy = [tuple(map(int, input().split())) for _ in range(m)]


    uf = UnionFind(n)
    for x, y in xy:
        uf.unite(x, y)

    b = sorted(enumerate(a), key=lambda x: x[1])
    i = 0
    j = 1
    cost = 0
    selected = [False] * n
    while True:
        u, cu = b[i]
        while j < n:
            v, cv = b[j]
            if uf.find(u) != uf.find(v):
                break
            j += 1
        if j == n: break
        uf.unite(u, v)
        cost += cu + cv
        selected[i] = selected[j] = True
        while i < n and selected[i]:
            i += 1
        if i == n: break
        j = max(j, i + 1)

    root = [uf.find(i) for i in range(n)]
    if len(set(root)) > 1:
        print('Impossible')
        return
    print(cost)

main()
