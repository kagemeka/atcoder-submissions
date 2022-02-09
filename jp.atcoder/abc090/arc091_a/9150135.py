import sys

n, m = map(int, sys.stdin.readline().split())
if n > m:
    n, m = m, n

def main():
    if n == 1:
        if m == 1:
            return 1
        else:
            return m - 2
    else:
        return (n - 2) * (m - 2)

if __name__ == '__main__':
    ans = main()
    print(ans)
