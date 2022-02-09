import sys
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
a, b, c = I[2:].reshape(-1, 3).T
a -= 1; b -= 1
c = np.negative(c)
graph = np.zeros((n, n))
graph[a, b] = c

def main():
    try:
        dist = bellman_ford(csgraph=csr_matrix(graph), directed=True, indices=0)
        return int(-dist[n-1])
    except:
        return 'inf'

if __name__ == '__main__':
    ans = main()
    print(ans)
