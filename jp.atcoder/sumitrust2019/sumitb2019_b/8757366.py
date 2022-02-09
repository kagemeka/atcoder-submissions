import sys
from math import ceil

def main():
    n = int(sys.stdin.readline().rstrip())
    x = ceil(n / 1.08)

    res = []
    while x * 27 // 25 == n:
        res.append(x)
        x += 1
    if res:
        print(res[0])
    else:
        print(':(')

if __name__ == '__main__':
    main()
