import sys
import numpy as np
import scipy.sparse


def main() -> None:
    n, m, s, t, *latter = map(int, sys.stdin.read().split())
    x, y, d = np.array(latter).reshape(m, 3).T
    csgraph = scipy.sparse.csr_matrix((d, (x - 1, y - 1)), shape=(n, n))
    dist = scipy.sparse.csgraph.shortest_path(
        csgraph,
        directed=False,
        indices=(s - 1, t - 1),
    )
    indices = np.argwhere((dist[0] == dist[1]) & (dist[0] != np.inf))
    print(-1 if not indices.size else indices[0, 0] + 1)


if __name__ == "__main__":
    main()
