import sys
import numpy as np
def main():
    hw = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(2, 2)

    if np.any(hw[0] - hw[1][0] == 0) or np.any(hw[0] - hw[1][1] == 0):
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
