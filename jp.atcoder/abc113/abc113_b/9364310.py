import sys

n, T, A, *h = map(int, sys.stdin.read().split())

def main():
    t = [T - 0.006 * h[i] for i in range(n)]
    d = [(abs(A - t[i]), i+1) for i in range(n)]
    d.sort()
    return d[0][1]

if __name__ == '__main__':
    ans = main()
    print(ans)
