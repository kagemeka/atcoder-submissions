import sys
import numpy as np

n, m = map(int, sys.stdin.readline().split())
A = np.array([list(sys.stdin.readline().rstrip()) for _ in range(n)], dtype='U1')
B = np.array([list(sys.stdin.readline().rstrip()) for _ in range(m)], dtype='U1')

def main():

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if np.all(A[i:i+m, j:j+m] == B):
                return 'Yes'
    return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
