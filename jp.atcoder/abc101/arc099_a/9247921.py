import sys

n, k, *a = map(int, sys.stdin.read().split())

def main():
    return ((n - 1) + (k - 1) - 1) // (k - 1)

if __name__ == '__main__':
    ans = main()
    print(ans)
