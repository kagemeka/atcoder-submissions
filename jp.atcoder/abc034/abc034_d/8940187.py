import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.float64)
n, k = I[:2].astype(np.int64)
water, percent = I[2:].reshape(-1, 2).T

def main():
    solt = water * percent / 100
    w = s = 0
    for _ in range(k):
        nex = (s + solt) / (w + water) * 100
        i = np.argmax(nex)
        w += water[i]
        s += solt[i]
        water[i] = np.inf
        solt[i] = 0

    ans = s / w * 100
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
