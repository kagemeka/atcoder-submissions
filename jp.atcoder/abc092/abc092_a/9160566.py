import sys

a, b, c, d = map(int, sys.stdin.read().split())

def main():
    return min(a, b) + min(c, d)

if __name__ == '__main__':
    ans = main()
    print(ans)
