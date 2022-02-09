# 2019-11-24 16:35:46(JST)
import sys
# import numpy as np
import itertools

def main():
    n = int(sys.stdin.readline().rstrip())
    cand = sorted(''.join(c) for c in itertools.product('abc', repeat=n))

    print('\n'.join(cand))

if __name__ == '__main__':
    main()
