import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
r = np.sort(I[1:])

def main():
    s = r ** 2 * np.pi
    s[1:] -= s[:-1]
    ans = np.sum(s[-1::-2])
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
