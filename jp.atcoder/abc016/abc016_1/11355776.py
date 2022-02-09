import sys

m, d = map(int, sys.stdin.readline().split())

def main():
    ans = 'NO' if m % d else 'YES'
    print(ans)

if __name__ ==  '__main__':
    main()
