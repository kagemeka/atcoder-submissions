import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
a = I[1:]

def main():
    i = np.argmax(np.absolute(a))

    if a[i] == 0:
        print(0)
        sys.exit()

    print(n * 2)
    res1 = np.concatenate((np.full(3, i+1)[:, None], np.arange(1, n+1)[:, None]), axis=1)
    if a[i] > 0:
        res2 = np.concatenate((np.arange(1, n)[:, None], np.arange(2, n+1)[:, None]), axis=1)
    else:
        res2 = np.concatenate((np.arange(n, 1)[:, None], np.arange(n-1, 0)[:, None]), axis=1)

    return np.concatenate((res1, res2))

if __name__ == '__main__':
    ans = main()
    for op in ans:
        print(*op, sep=' ')
