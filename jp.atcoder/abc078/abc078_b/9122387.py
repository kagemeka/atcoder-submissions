import sys

L, l, d = map(int, sys.stdin.readline().split())

def main():
    x = (L - d) // (l + d)
    return x

if __name__ == '__main__':
    ans = main()
    print(ans)
