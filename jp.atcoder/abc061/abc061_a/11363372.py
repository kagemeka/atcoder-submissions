import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if a <= c <= b else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
