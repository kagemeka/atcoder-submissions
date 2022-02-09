import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    print(max(0, b + c - a))

if __name__ ==  '__main__':
    main()
