import sys

w, h, x, y = map(int, sys.stdin.readline().split())

def main():
    s = w * h / 2
    f = (x == w / 2 and y == h / 2) & 1
    return s, f

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
