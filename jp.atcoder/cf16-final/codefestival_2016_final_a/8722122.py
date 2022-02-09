import sys
import numpy as np
from string import ascii_uppercase as alphabet

def main():
    H, W = map(int, sys.stdin.readline().split())
    table = np.array(sys.stdin.read().split(), dtype='U5').reshape(H, W)

    for i in range(H):
        for j in range(W):
            if table[i][j] == 'snuke':
                ans = alphabet[j] + str(i+1)
                print(ans)
                sys.exit()

if __name__ == '__main__':
    main()
