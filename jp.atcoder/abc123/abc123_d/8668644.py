import sys
import numpy as np

def main():
    x, y, z, K = map(int, sys.stdin.readline().split())
    abc = np.array(sys.stdin.read().split(), dtype=np.int64)
    a = abc[:x]
    b = abc[x:x + y]
    c = abc[x + y:x + y+ z]

    ab = np.sort(np.array([a[i] + b for i in range(x)]).reshape(-1))[::-1][:K]
    res = np.sort(np.array([c[i] + ab for i in range(z)]).reshape(-1))[::-1][:K]

    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
