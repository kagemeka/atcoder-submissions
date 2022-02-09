import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if m == n else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
