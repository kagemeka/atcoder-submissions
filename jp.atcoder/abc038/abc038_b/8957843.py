import sys
import numpy as np

d1, d2 = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2)

def main():
    if np.any(d1 == d2) or np.any(d1 == d2[::-1]):
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
