import typing
import sys
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    # compute Ex in case that any paths are not blocked.
    # for each edge e,
    # Ex = probability(pass through e) * Ex(in case pass through e) + probability(not pass through e) * Ex(in case not pass through e)
    # preprocess the probability passing through each node.

    # N -> all: OK
    # 1 -> all: may by NG.
    # remove nodes not contained in any paths from 1 to N.
    # strongly connected components.

    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    rev_g = [[] for _ in range(n)]
    in_deg = [0] * n

    st = []
    for _ in range(m):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        st.append((s, t))
        g[s].append(t)
        in_deg[t] += 1
        rev_g[t].append(s)

    prob = [[0] * n for _ in range(n)]
    for i in range(n):
        k = len(g[i])
        for j in g[i]:
            prob[i][j] = 1 / k

    inf = 1 << 60
    # Ex for each node -> N
    count = [inf] * n
    for u in range(n - 1, -1, -1):
        ex = 0
        for v in g[u]:
            ex += prob[u][v] * (count[v] + 1)
        count[u] = ex

    prob_node = [0] * n
    prob_node[0] = 1
    que = [i for i in range(n) if in_deg[i] == 0]
    for u in que:
        for v in g[u]:
            prob_node[v] += prob_node[u] * prob[u][v]
            in_deg[v] -= 1
            if in_deg[v] == 0: que.append(v)

    mn = count[0]
    for i, j in st:
        if len(g[i]) == 1: continue
        ex = count[0] - prob_node[i] * (count[i] - (count[i] - prob[i][j] * (count[j] + 1)) * len(g[i]) / (len(g[i]) - 1))
        mn = min(mn, ex)
    print(mn)





main()
