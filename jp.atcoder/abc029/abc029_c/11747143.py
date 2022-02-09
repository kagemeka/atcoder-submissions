import sys
from itertools import product

n = int(sys.stdin.readline().rstrip())

def main():
    print(*[''.join(s) for s in product('abc', repeat=n)], sep='\n')

if __name__ ==  '__main__':
    main()
