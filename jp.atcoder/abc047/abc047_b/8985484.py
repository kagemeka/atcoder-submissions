import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
w, h, n = I[:3]
x, y, a = I[3:].reshape(n, 3).T

def main():
    l = 0
    r = w
    d = 0
    u = h
    if np.any(a == 1):
        l = np.amax(x[a == 1])
    if np.any(a == 2):
        r = np.amin(x[a == 2])
    if np.any(a == 3):
        d = np.amax(y[a == 3])
    if np.any(a == 4):
        u = np.amin(y[a == 4])

    if l > r or d > u:
        return 0
    return (r - l) * (u - d)

if __name__ == '__main__':
    ans = main()
    print(ans)
