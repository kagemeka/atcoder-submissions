import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

n = int(sys.stdin.readline().rstrip())
xy = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2).T


def main():
    indices1, indices2 = np.argsort(xy)
    res1 = xy[:, indices1]
    res2 = xy[:, indices2]
    d1 = np.absolute(res1[:, 1:] - res1[:, :-1])
    d1 = np.amin(d1, axis=0)
    d2 = np.absolute(res2[:, 1:] - res2[:, :-1])
    d2 = np.amin(d2, axis=0)

    graph = np.full((n, n), np.inf)
    a1 = indices1[:-1]
    b1 = indices1[1:]
    a2 = indices2[:-1]
    b2 = indices2[1:]

    graph[a1, b1] = d1
    graph[a2, b2] = np.minimum(graph[a2, b2], d2)
    graph[graph == np.inf] = 0
    graph = csr_matrix(graph)

    t = minimum_spanning_tree(graph)
    ans = np.sum(t)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
