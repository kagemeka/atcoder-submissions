import sys

a, b, x = map(int, sys.stdin.readline().split())

def main():
    ans = 'YES' if a <= x <= a + b else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
