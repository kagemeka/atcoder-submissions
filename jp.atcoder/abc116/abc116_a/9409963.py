import sys

c, a, b = map(int, sys.stdin.readline().split())

def main():
    return c * a // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
