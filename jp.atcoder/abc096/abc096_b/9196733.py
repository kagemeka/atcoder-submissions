import sys

*a, k = map(int, sys.stdin.read().split())

def main():
    a.sort()
    return sum(a[:2]) + a[-1] * 2 ** k

if __name__ == '__main__':
    ans = main()
    print(ans)
