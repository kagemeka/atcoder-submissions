import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = -1 if a >= 10 or b >= 10 else a * b
    print(ans)

if __name__ ==  '__main__':
    main()
