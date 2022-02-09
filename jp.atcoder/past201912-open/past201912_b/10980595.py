import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    prev = a[0]
    for cur in a[1:]:
        d = cur - prev
        if d == 0:
            yield 'stay'
        elif d > 0:
            yield 'up {0}'.format(d)
        else:
            yield 'down {0}'.format(-d)
        prev = cur

if __name__ == "__main__":
    ans = main()
    print(*ans, sep='\n')
