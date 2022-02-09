import sys

n, *c = map(int, sys.stdin.read().split())

def main():
    c.sort()
    return c[-1] - c[0]

if __name__ == '__main__':
    ans = main()
    print(ans)
