import sys

w, h, x, y = map(int, sys.stdin.readline().split())

def main():
    s = w * h / 2
    t = x * 2 == w and y * 2 == h; t *= 1
    print(s, t)

if __name__ ==  '__main__':
    main()
