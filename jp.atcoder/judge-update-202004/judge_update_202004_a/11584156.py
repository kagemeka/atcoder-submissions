import sys

s, l, r = map(int, sys.stdin.readline().split())

def main():
    print(min(r, max(l, s)))

if __name__ == '__main__':
    main()
