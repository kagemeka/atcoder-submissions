import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return 'Yes' if a * b & 1 else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
