import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    ans = c // min(a, b)
    print(ans)

if __name__ ==  '__main__':
    main()
