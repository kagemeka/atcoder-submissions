import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
c, p = np.array(sys.stdin.read().split()).reshape(-1, 2).T
p = p.astype(np.int64)

def main():
    i = np.argmax(p)
    s = np.sum(p)
    if p[i] > s / 2:
        return c[i]
    return 'atcoder'

if __name__ == '__main__':
    ans = main()
    print(ans)
