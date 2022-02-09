import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return 'Odd' if a * b & 1 else 'Even'

if __name__ == '__main__':
    ans = main()
    print(ans)
