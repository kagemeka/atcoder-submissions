import sys
from math import ceil

def main():
    n, *cap = map(int, sys.stdin.read().split())

    t = ceil(n / min(cap) + 4)
    print(t)
if __name__ == "__main__":
    main()
