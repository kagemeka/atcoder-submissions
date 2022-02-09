import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    return 'YES' if b - a == c - b else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
