import sys

h, w, n = map(int, sys.stdin.read().split())
if h < w:
        h, w = w, h

def main():
    return (n + h - 1) // h

if __name__ == '__main__':
    ans = main()
    print(ans)
