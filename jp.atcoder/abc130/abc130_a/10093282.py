import sys

x, a = map(int, sys.stdin.readline().split())

def main():
    return ((x >= a) & 1) * 10

if __name__ == '__main__':
    ans = main()
    print(ans)
