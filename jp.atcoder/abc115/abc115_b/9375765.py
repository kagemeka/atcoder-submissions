import sys

n, *p = map(int, sys.stdin.read().split())

def main():
    return sum(p) - max(p) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
