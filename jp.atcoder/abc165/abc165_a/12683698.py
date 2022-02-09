import sys

k, a, b = map(int, sys.stdin.read().split())

def main():
    ans = 'OK' if (a + k - 1) // k  * k <= b else 'NG'
    print(ans)

if __name__ == '__main__':
    main()
