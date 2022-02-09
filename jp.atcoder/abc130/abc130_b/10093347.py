import sys

n, b, *l = map(int, sys.stdin.read().split())

def main():
    d = 0
    for i in range(n):
        d += l[i]
        if d > b:
            return i + 1
    return n + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
