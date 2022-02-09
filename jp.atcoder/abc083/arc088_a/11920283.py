import sys

x, y = map(int, sys.stdin.readline().split())

def main(x):
    cnt = 0
    while x <= y:
        cnt += 1
        x *= 2
    print(cnt)

if __name__ ==  '__main__':
    main(x)
