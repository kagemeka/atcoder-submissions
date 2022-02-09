import sys

n, a = map(int, sys.stdin.read().split())

def main():
    return 'Yes' if a > n % 500 else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
