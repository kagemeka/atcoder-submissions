import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
    m = len(g)
    g = np.vstack((g, g))
    g[m:, :2] = g[m:, 1::-1]
    return g


@nb.njit
def sort_csgraph(n: int, g: np.ndarray) -> typing.Tuple[(np.ndarray, ) * 3]:
    idx = g[:, 0] << 30 | g[:, 1]
    sort_idx = np.argsort(idx, kind='mergesort')
    g = g[sort_idx]
    original_idx = np.arange(len(g))[sort_idx]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    return g, edge_idx, original_idx



@nb.njit
def connected_components_dfs(n: int, g: np.ndarray):
    g = csgraph_to_directed(g)
    g, edge_idx, _ = sort_csgraph(n, g)
    label = np.full(n, -1, np.int64)
    l = 0
    for i in range(n):
        if label[i] != -1: continue
        label[i] = l
        st = [i]
        while st:
            u = st.pop()
            for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
                if label[v] != -1: continue
                label[v] = l
                st.append(v)
        l += 1
    return label



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, uv: np.ndarray) -> typing.NoReturn:
    m = len(uv)
    if n != m:
        print(0)
        return
    mod = 998_244_353
    edge_cnt = np.zeros(n, np.int64)
    for i in range(m):
        u, v = uv[i]
        edge_cnt[u] += 1
        edge_cnt[v] += 1
    label = connected_components_dfs(n, uv)

    k = label.max() + 1
    edge_cnt2 = np.zeros(k, np.int64)
    for i in range(n):
        edge_cnt2[label[i]] += edge_cnt[i]

    b = np.bincount(label)
    if not np.all(b * 2 == edge_cnt2):
        print(0)
        return
    res = 1
    for _ in range(label.max() + 1):
        res = res * 2 % mod
    print(res)


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    uv = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(m, 2) - 1
    solve(n, uv)


main()
