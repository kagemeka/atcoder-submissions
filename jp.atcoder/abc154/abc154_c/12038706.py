import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    print("YES" if len(set(a)) == n else "NO")

if __name__ ==  '__main__':
    main()
