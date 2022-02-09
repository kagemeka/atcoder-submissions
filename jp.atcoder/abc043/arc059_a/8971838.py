import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
a = I[1:]

def main():
    m = int(np.around(np.mean(a)))
    ans = np.sum((a - m) ** 2)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
