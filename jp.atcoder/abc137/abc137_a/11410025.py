import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    print(max(a+b, a-b, a*b))

if __name__ ==  '__main__':
    main()
