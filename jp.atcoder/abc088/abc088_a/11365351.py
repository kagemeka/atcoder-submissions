import sys

n, a = map(int, sys.stdin.read().split())

def main():
    r = n % 500
    ans = 'Yes' if r <= a else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
