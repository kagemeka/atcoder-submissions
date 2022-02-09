import sys

n, a = map(int, sys.stdin.read().split())

def main():
    return n ** 2 - a

if __name__ == '__main__':
    ans = main()
    print(ans)
