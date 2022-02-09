import sys

a, b, t = map(int, sys.stdin.readline().split())

def main():
    return b * (t // a)

if __name__ == '__main__':
    ans = main()
    print(ans)
