import sys
import numpy as np

n, a, b = map(int, sys.stdin.readline().split())
s, d = np.array(sys.stdin.read().split()).reshape(-1, 2).T
d = d.astype(np.int64)

def main():
    d[d < a] = a
    d[d > b] = b
    w = s == 'West'
    d[w] = np.negative(d[w])
    res = np.sum(d)

    if res == 0:
        return 0
    elif res > 0:
        return 'East {0}'.format(res)
    else:
        return 'West {0}'.format(abs(res))

if __name__ == '__main__':
    ans = main()
    print(ans)
