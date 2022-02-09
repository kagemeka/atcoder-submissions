import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n = I[0]
t = I[1:1+n]
m = I[1+n]
p, x = I[2+n:].reshape(m, 2).T

def main():
    default = np.sum(t)
    res = default + (x - t[p-1])
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
