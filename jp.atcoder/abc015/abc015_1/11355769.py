import sys

a, b = sys.stdin.read().split()

def main():
    ans = a if len(a) > len(b) else b
    print(ans)

if __name__ == '__main__':
    main()
