import sys

x, a, b = map(int, sys.stdin.read().split())

def main():
    return (x - a) % b

if __name__ == '__main__':
    ans = main()
    print(ans)
