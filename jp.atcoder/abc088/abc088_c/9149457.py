import sys
import numpy as np

c = np.array(sys.stdin.read().split(), dtype=np.int8).reshape(3, 3)

def main(c):
    c -= c[0]
    c -= c[:, 0][:, None]
    return 'No' if np.count_nonzero(c) else 'Yes'

if __name__ == '__main__':
    ans = main(c)
    print(ans)
