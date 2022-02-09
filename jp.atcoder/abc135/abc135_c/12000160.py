import sys

n = int(sys.stdin.readline().rstrip())
*a, = map(int, sys.stdin.readline().split())
*b, = map(int, sys.stdin.readline().split())

def main():
    tot = 0
    for i in range(n):
        tot += min(b[i], a[i])
        b[i] = max(0, b[i] - a[i])
        tot += min(b[i], a[i+1])
        a[i+1] = max(0, a[i+1] - b[i])
    print(tot)

if __name__ ==  '__main__':
    main()
