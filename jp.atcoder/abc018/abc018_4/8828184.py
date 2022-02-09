import sys
from itertools import combinations
import numpy as np

I = np.array(sys.stdin.read().split(), np.int64)
n, m, p, q, r = I[:5]
x, y, z = I[5:].reshape(-1, 3).T

graph = np.zeros((n, m), np.int64)
graph[x-1, y-1] = z

def main():
    girls = np.array(list(combinations(range(n), p)), np.int64)

    res = np.sum(graph[girls], axis=1)
    res = np.sort(res, axis=1)
    res = np.sum(res[:, -q:], axis=1)
    ans = np.amax(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
