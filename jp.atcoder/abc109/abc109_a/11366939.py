import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if a * b & 1 else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
