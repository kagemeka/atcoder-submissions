import sys

n = int(sys.stdin.readline().rstrip())
xg = [sys.stdin.readline().split() for _ in range(n)]

def main():
    xg.sort(key=lambda x: int(x[0]))
    xg.sort(key=lambda x: x[1], reverse=True)
    for x, g in xg:
        print(x)

if __name__ == '__main__':
    main()
