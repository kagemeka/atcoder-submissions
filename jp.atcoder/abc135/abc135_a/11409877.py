import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    d = abs(b - a)
    if d & 1:
        ans = "IMPOSSIBLE"
    else:
        ans = min(a, b) + d // 2
    print(ans)

if __name__ ==  '__main__':
    main()
