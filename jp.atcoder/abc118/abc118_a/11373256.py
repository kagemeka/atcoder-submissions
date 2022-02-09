import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = a + b if not b % a else b - a
    print(ans)

if __name__ ==  '__main__':
    main()
