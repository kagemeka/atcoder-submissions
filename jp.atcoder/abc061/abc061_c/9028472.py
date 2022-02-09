import sys

n, k, *ab = map(int, sys.stdin.read().split())
ab = zip(*[iter(ab)] * 2)

def main():
    s = 0
    for a, b in ab:
        s += b
        if s >= k:
            return a

if __name__ == '__main__':
    ans = main()
    print(ans)
