import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main(a, b, c, d):
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            return
        a -= d
        if a <= 0:
            print('No')
            return



if __name__ == '__main__':
    main(a, b, c, d)
