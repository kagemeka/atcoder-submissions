import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    return max(0, min(b, d) - max(a, c))

if __name__ == '__main__':
    ans = main()
    print(ans)
