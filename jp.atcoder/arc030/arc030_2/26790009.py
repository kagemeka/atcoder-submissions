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
    idx = (g[:, 0] << 30) + g[:, 1]
    sort_idx = np.argsort(idx, kind='mergesort')
    g = g[sort_idx]
    original_idx = np.arange(len(g))[sort_idx]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    return g, edge_idx, original_idx


@nb.njit
def euler_tour_edge(
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> typing.Tuple[(np.ndarray, ) * 3]:
    n = g[:, :2].max() + 1
    parent = np.full(n, -1, np.int64)
    depth = np.zeros(n, np.int64)
    tour = np.empty(n << 1, np.int64)
    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0: continue
        st.append(~u)
        for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
            if v == parent[u]: continue
            parent[v] = u
            depth[v] = depth[u] + 1
            st.append(v)
    return tour, parent, depth


@nb.njit((nb.i8[:, :], nb.i8[:], nb.i8), cache=True)
def solve(ab: np.ndarray, h: np.ndarray, x: int) -> typing.NoReturn:
    n = len(h)
    # assert np.all(np.unique(ab) == np.arange(n))
    g, edge_idx, _ = sort_csgraph(n, csgraph_to_directed(ab))
    tour, parent, _ = euler_tour_edge(g, edge_idx, x)

    # cost = np.zeros(n, np.int64)
    # found = np.zeros(n, np.bool8)
    # for u in tour:
    #     if u >= 0: continue
    #     u = ~u
    #     found[u] |= h[u]
    #     p = parent[u]
    #     if p == -1 or not found[u]: continue
    #     cost[p] += cost[u] + 2
    #     found[p] |= found[u]
    # print(cost[x])


def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    x -= 1
    h = np.array(sys.stdin.readline().split(), dtype=np.int64)
    ab = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n - 1, 2) - 1
    solve(ab, h, x)


main()
