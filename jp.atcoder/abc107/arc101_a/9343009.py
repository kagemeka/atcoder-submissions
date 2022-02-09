import sys

n, k, *x = map(int, sys.stdin.read().split())

def main():
    l = 0; r = k - 1
    ans = float('inf')
    while r < n:
        if x[r] <= 0:
            res = abs(x[l])
        elif x[l] < 0:
            res = min(abs(x[l]), x[r]) * 2 + max(abs(x[l]), x[r])
        else:
            res = x[r]
        ans = min(ans, res)
        l += 1; r += 1

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
