import sys

n, k, *h = map(int, sys.stdin.read().split())

def main():
    h.sort()

    res = float('inf')
    for i in range(n-k+1):
        res = min(res, h[i+k-1] - h[i])

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
