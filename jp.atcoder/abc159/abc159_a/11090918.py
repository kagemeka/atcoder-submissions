import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    res = n * (n - 1) // 2 + m * (m - 1) // 2
    return res

if __name__ == "__main__":
    ans = main()
    print(ans)
