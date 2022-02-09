import sys

n, i = map(int, sys.stdin.readline().split())

def main():
    return n + 1 - i

if __name__ == '__main__':
    ans = main()
    print(ans)
