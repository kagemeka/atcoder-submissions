import sys

n, a, b = map(int, sys.stdin.readline().split())

def main():
    print(min(a*n, b))

if __name__ ==  '__main__':
    main()
