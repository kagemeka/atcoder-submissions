import sys

n, a, b = map(int, sys.stdin.readline().split())

def main():
    d = b - a
    if d % 2 == 0:
        return d // 2
    else:
        return min(n - b, abs(1 - a)) + 1 + (d - 1) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
