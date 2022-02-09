import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from itertools import permutations

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m, R = I[:3]
r = I[3:3+R] - 1
a, b, c = I[3+R:].reshape(-1, 3).T
a -= 1; b -= 1
graph = csr_matrix((c, (a, b)), shape=(n, n))

def main():
    dist = floyd_warshall(graph, directed=False).astype(np.int64)
    *perms, = permutations(r)
    perms = np.array(perms)
    res = dist[perms[:, :-1], perms[:, 1:]]
    ans = np.amin(np.sum(res, axis=1))
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
