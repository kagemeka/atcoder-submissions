import sys

*a, = map(int, sys.stdin.readline().split())

def main():
    a.sort()
    return a[1]

if __name__ == '__main__':
    ans = main()
    print(ans)
