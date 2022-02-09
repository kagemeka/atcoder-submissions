import sys

def main():
    n, a = map(int, sys.stdin.read().split())
    print('Yes' if n % 500 <= a else 'No')

if __name__ == "__main__":
    main()
