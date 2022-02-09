import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = 'Odd' if a*b & 1 else 'Even'
    print(ans)

if __name__ ==  '__main__':
    main()
