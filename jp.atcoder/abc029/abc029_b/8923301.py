import sys
import numpy as np

s = np.array(sys.stdin.read().split(), dtype='U')

def main():
    c = np.char.count(s, 'r')
    ans = np.count_nonzero(c)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
