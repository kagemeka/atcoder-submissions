import sys

*p, = map(int, sys.stdin.readline().split())

def main():
    p.sort()
    return sum(p[:2])

if __name__ == '__main__':
    ans = main()
    print(ans)
