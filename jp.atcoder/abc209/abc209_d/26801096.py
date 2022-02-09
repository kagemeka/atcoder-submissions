import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def euler_tour_edge(
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> typing.Tuple[(np.ndarray, ) * 3]:
    n = 1 if len(g) == 0 else g[:, :2].max() + 1
    parent = np.full(n, -1, np.int64)
    depth = np.zeros(n, np.int64)
    tour = np.empty(n << 1, np.int64)
    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0:
            continue
        st.append(~u)
        for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            st.append(v)
    return tour, parent, depth


@nb.njit
def tree_bfs(
    g: np.ndarray,
    edge_idx: np.ndarray,
    root: int,
) -> typing.Tuple[(np.ndarray, ) * 2]:
    n = g[:, :2].max() + 1
    parent = np.full(n, -1, np.int64)
    depth = np.zeros(n, np.int64)
    fifo_que = [root]
    for u in fifo_que:
        for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
            if v == parent[u]: continue
            parent[v] = u
            depth[v] = depth[u] + 1
            fifo_que.append(v)
    return parent, depth


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


@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(ab: np.ndarray, cd: np.ndarray) -> typing.NoReturn:
    n = len(ab) + 1
    q = len(cd)
    g, edge_idx, _ = sort_csgraph(n, csgraph_to_directed(ab))
    _, _, depth = euler_tour_edge(g, edge_idx, 0)
    # _, depth = tree_bfs(g, edge_idx, 0)
    for i in range(q):
        c, d = cd[i]
        if (depth[c] - depth[d]) & 1:
            print('Road')
        else:
            print('Town')



def main() -> typing.NoReturn:
  n, q = map(int, input().split())
  tmp = np.array(
      sys.stdin.read().split(),
      dtype=np.int64,
  ).reshape(-1, 2) - 1
  ab, cd = tmp[:n - 1], tmp[n - 1:]
  solve(ab, cd)


main()
