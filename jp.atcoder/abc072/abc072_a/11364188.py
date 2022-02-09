import sys

x, t = map(int, sys.stdin.readline().split())

def main():
    print(max(0, x - t))

if __name__ ==  '__main__':
    main()
