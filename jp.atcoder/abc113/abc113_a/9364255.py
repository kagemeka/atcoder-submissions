import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    return x + y // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
