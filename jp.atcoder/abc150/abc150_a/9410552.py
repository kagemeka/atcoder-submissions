import sys

k, x = map(int, sys.stdin.readline().split())

def main():
    return 'Yes' if 500 * k >= x else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
