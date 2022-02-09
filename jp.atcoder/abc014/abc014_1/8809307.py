import sys

a, b = map(int, sys.stdin.read().split())

def main():
    return (b - a % b) % b

if __name__ == '__main__':
    ans = main()
    print(ans)
