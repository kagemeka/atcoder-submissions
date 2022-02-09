import sys

a, b, c, k = map(int, sys.stdin.readline().split())

def main():
    if k <= a + b:
        print(min(a, k))
    else:
        print(a - (k - (a + b)))
if __name__ == '__main__':
    main()
