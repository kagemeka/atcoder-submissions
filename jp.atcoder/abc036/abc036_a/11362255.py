import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = (b + a - 1) // a
    print(ans)

if __name__ ==  '__main__':
    main()
