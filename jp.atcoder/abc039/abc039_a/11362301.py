import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    s = 2 * (a * b + b * c + c * a)
    print(s)

if __name__ ==  '__main__':
    main()
