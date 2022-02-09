import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, ma, mb = I[:3]
abc = I[3:].reshape(n, 3)

def main():
    sa, sb = np.sum(abc, axis=0)[:2]
    res = np.full((sa+1, sb+1), np.inf)
    res[0, 0] = 0

    for a, b, c in abc:
        res[a:, b:] = np.minimum(res[a:, b:], res[:-a, :-b] + c)

    ans = np.inf
    for i in range(1, min(sa//ma, sb//mb) + 1):
        ans = np.minimum(ans, res[ma * i, mb * i])

    if ans == np.inf:
        return -1
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
