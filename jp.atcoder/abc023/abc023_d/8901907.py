import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
H, S = I[1:].reshape(-1, 2).T.astype(np.float64)

def main():
    h, s = H, S
    res = np.zeros(n)
    for _ in range(n):
        h += s
        i = np.argmax(h)
        res[i] = h[i] - s[i]
        h[i] = -np.inf
    ans = np.amax(res)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
