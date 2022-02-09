import sys

n, *ab = map(int, sys.stdin.read().split())
ab = zip(*[iter(ab)] * 2)

def main():
    sa = sb = 0
    for a, b in ab:
        if a > b:
            sa += a + b
        elif a < b:
            sb += a + b
        else:
            sa += a
            sb += b
    return sa, sb

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
