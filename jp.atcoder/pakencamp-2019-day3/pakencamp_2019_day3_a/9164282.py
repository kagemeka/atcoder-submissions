import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return b - a + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
