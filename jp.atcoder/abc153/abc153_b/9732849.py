import sys

h, n, *a = map(int, sys.stdin.read().split())

def main():
    return 'Yes' if sum(a) >= h else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
