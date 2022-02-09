import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    c = a + b
    return 'IMPOSSIBLE' if c & 1 else c // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
