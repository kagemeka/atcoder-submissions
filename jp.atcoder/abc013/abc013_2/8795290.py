import sys

a, b = map(int, sys.stdin.read().split())

def main():
    d = abs(b - a)
    return min(d, 10 - d)

if __name__ == '__main__':
    ans = main()
    print(ans)
