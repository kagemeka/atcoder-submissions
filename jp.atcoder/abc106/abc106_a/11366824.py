import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = a * b - (a + b - 1)
    print(ans)

if __name__ ==  '__main__':
    main()
