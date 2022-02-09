import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    return 'Yes' if a + b >= c else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
