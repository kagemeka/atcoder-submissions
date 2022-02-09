import sys
from itertools import product

n = int(sys.stdin.readline().rstrip())

def main():
    print(*map(lambda s: ''.join(s), product('abc', repeat=n)), sep='\n')

if __name__ ==  '__main__':
    main()
