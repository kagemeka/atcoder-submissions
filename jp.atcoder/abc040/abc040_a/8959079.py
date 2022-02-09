import sys

n, x = map(int, sys.stdin.readline().split())

def main():
    ans = min(x - 1, n - x)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
