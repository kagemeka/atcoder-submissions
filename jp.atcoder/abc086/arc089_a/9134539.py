import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
txy = I[1:].reshape(-1, 3)

def main():
    t1, x1, y1 = txy[0]
    d1 = x1 + y1
    if d1 > t1 or (t1 - d1) & 1:
        return 'No'
    dt, dx, dy = np.absolute(np.transpose(txy[1:] - txy[:-1]))
    d = dx + dy

    return 'No' if np.any(np.logical_or(d > dt, (dt - d) & 1)) else 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
