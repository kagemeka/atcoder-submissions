import sys

n, a, b = map(int, sys.stdin.readline().split())

def main():
    return min(a * n, b)

if __name__ == '__main__':
    ans = main()
    print(ans)
