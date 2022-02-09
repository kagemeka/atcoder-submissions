import sys
from math import ceil

n, *cap = map(int, sys.stdin.read().split())

def main():
    return 4 + ceil(n / min(cap))

if __name__ == '__main__':
    ans = main()
    print(ans)
