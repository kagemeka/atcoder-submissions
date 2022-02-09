import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    a.sort()
    return a[-1] - a[0]

if __name__ == '__main__':
    ans = main()
    print(ans)
