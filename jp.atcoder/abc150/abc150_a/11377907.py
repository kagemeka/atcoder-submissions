import sys

k, x = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if 500*k >= x else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
