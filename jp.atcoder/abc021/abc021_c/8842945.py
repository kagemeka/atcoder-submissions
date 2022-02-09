import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

MOD = 10 ** 9 + 7

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, a, b, m = I[:4]
a -= 1; b -= 1
x, y = I[4:].reshape(-1, 2).T
G = np.zeros((n, n), dtype=np.int64)
G[x-1, y-1] += 1; G[y-1, x-1] += 1

def main():
    dist = dijkstra(csgraph=csr_matrix(G), directed=False, indices=a).astype(np.int64)
    path_cnt = np.zeros(n, dtype=np.int64)
    path_cnt[a] = 1
    for d in range(1, dist[b] + 1):
        v = np.where(dist == d)[0]
        u = np.where(dist == d - 1)[0]
        path_cnt[v] = np.sum(path_cnt[u] * G[:, u][v], axis=1)
        path_cnt[v] %= MOD

    return path_cnt[b]

if __name__ == '__main__':
    ans = main()
    print(ans)
