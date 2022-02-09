import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    c = sorted(set(a))
    print(c[-2])

if __name__ == '__main__':
    main()
