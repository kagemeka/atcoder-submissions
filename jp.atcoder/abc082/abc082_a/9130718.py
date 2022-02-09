import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return ((a + b) + 2 - 1) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
