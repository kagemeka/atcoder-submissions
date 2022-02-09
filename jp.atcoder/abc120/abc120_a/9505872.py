import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    return min(b // a, c)

if __name__ == '__main__':
    ans = main()
    print(ans)
