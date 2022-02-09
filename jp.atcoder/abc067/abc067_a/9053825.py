import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return 'Impossible' if a % 3 and b % 3 and (a + b) % 3 else 'Possible'

if __name__ == '__main__':
    ans = main()
    print(ans)
