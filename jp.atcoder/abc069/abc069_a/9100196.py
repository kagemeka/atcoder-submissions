import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    return (n - 1) * (m - 1)

if __name__ == '__main__':
    ans = main()
    print(ans)
