import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    return 'Yes' if n == m else ' No'

if __name__ == '__main__':
    ans = main()
    print(ans)
