import sys
from itertools import product

s, n = sys.stdin.read().split()
n = int(n)

def main():
    *res, = product(s, repeat=2)
    print(''.join(res[n-1]))

if __name__ ==  '__main__':
    main()
