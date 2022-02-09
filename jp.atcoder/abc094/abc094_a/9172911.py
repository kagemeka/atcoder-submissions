import sys

a, b, x = map(int, sys.stdin.readline().split())

def main():
    return 'YES' if a <= x <= a + b else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
