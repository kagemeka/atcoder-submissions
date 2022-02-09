import typing
import numpy as np
import sys

def main() -> typing.NoReturn:
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    a = [None] * (m + 1)
    a[0] = np.identity(3, dtype=np.int64)
    for i in range(m):
        op = list(map(int, input().split()))
        if op[0] == 1:
            a[i + 1] = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
        elif op[0] == 2:
            a[i + 1] = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        elif op[0] == 3:
            a[i + 1] = np.array([[-1, 0, 2 * op[1]], [0, 1, 0], [0, 0, 1]])
        elif op[0] == 4:
            a[i + 1] = np.array([[1, 0, 0], [0, -1, 2 * op[1]], [0, 0, 1]])


    for i in range(m):
        a[i + 1] = a[i + 1].dot(a[i])

    q = int(input())
    bc = [tuple(map(int, input().split())) for _ in range(q)]
    for b, c in bc:
        x, y = xy[c - 1]
        arr = np.array([x, y, 1])
        arr = a[b].dot(arr)
        print(arr[0], arr[1])



main()
