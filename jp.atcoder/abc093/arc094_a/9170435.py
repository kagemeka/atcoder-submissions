import sys

*a, = map(int, sys.stdin.readline().split())

def main():
    a.sort()
    res = a[2] * 2 - a[0] - a[1]
    return (res + 3) // 2 if res & 1 else res // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
