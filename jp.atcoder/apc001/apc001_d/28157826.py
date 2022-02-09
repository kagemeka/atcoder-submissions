import typing
import collections


class UnionFind():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__data = [-1] * n

    def find(self, u: int) -> typing.NoReturn:
        d = self.__data
        if d[u] < 0: return u
        d[u] = self.find(d[u])
        return d[u]

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]

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
    # check the count of united nodes of the connected component after united.

    xy = [tuple(map(int, input().split())) for _ in range(m)]


    uf = UnionFind(n)
    for x, y in xy:
        uf.unite(x, y)

    b = sorted(enumerate(a), key=lambda x: x[1])
    i = 0
    j = 1
    cost = 0
    selected = [False] * n
    selected_cnt = [0] * n # per component.
    que = collections.deque()
    while True:
        while i < n and selected[i]:
            i += 1
        if i == n: break
        while que and que[0] == i:
            que.popleft()
        u, cu = b[i]
        j = max(j, i + 1)
        if uf.size(u) - selected_cnt[uf.find(u)] >= 2 and que:
            tmp = j
            j = que.popleft()
            v, cv = b[j]
            assert uf.find(u) != uf.find(v)
            cnt = selected_cnt[uf.find(u)] + selected_cnt[uf.find(v)]
            selected_cnt[uf.find(u)] = selected_cnt[uf.find(v)] = cnt
            uf.unite(u, v)
            selected_cnt[uf.find(u)] += 2
            cost += cu + cv
            selected[i] = selected[j] = True
            j = tmp
            continue

        while j < n:
            v, cv = b[j]
            if uf.find(u) == uf.find(v):
                j += 1
                continue
            cnt = uf.size(u) + uf.size(v) - selected_cnt[uf.find(u)] - selected_cnt[uf.find(v)]
            assert cnt >= 2
            if cnt == 2 and uf.size(u) + uf.size(v) != n:
                que.append(j)
                j += 1
                continue
            break
        if j >= n: break
        cnt = selected_cnt[uf.find(u)] + selected_cnt[uf.find(v)]
        selected_cnt[uf.find(u)] = selected_cnt[uf.find(v)] = cnt
        uf.unite(u, v)
        selected_cnt[uf.find(u)] += 2
        cost += cu + cv
        selected[i] = selected[j] = True
        j += 1


    root = [uf.find(i) for i in range(n)]
    if len(set(root)) > 1:
        print('Impossible')
        return
    print(cost)

main()
