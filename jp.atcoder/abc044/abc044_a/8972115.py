import sys

n, k, x, y = map(int, sys.stdin.read().split())

def main():
    if n > k:
        return x * k + y * (n - k)
    return x * n

if __name__ == '__main__':
    ans = main()
    print(ans)
