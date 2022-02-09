import sys

n, *p = map(int, sys.stdin.read().split())

def main():
    mi = float('inf')
    res = 0
    for i in range(n):
        if p[i] <= mi:
            res += 1
            mi = p[i]
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
