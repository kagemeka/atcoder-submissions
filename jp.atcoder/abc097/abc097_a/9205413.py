import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    return 'Yes' if abs(c - a) <= d or abs(b - a) <= d and abs(c - b) <= d else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
