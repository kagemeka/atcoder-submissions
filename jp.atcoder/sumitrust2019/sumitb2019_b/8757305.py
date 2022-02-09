import sys
from math import ceil, floor
def main():
    n = int(sys.stdin.readline().rstrip())
    x = ceil(n / 1.08)
    if floor(x * 1.08) == n:
        print(x)
    else:
        print(':(')
if __name__ == '__main__':
    main()
