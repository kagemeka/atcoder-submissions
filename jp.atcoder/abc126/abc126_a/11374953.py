import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def main():
    res = s[:k-1] + s[k-1].lower() + s[k:]
    print(res)

if __name__ ==  '__main__':
    main()
