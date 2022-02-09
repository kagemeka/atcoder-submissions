import sys

r, g = map(int, sys.stdin.read().split())

def main():
    return g * 2 - r

if __name__ == '__main__':
    ans = main()
    print(ans)
