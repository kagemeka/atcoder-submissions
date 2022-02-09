import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    print(sum(a) - n)

if __name__ ==  '__main__':
    main()
