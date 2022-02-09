import sys

m, d = map(int, sys.stdin.readline().split())

def main():
    return 'YES' if m % d == 0 else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
