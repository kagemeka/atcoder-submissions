import sys

h, a = map(int, sys.stdin.readline().split())

def main():
    print((h + a - 1) // a)

if __name__ ==  '__main__':
    main()
