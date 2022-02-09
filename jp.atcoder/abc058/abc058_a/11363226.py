import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    ans = 'YES' if b - a == c - b else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
