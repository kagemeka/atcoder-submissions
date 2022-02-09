import sys

x, y, z, K = map(int, sys.stdin.readline().split())
a, b, c = (sorted(map(int, sys.stdin.readline().split()), reverse=True) for _ in range(3))
def main():
    res = []
    for i in range(1, min(K, x) + 1):
        for j in range(1, min(K // i, y) + 1):
            for k in range(1, min(K // (i * j), z) + 1):
                res.append(a[i-1] + b[j-1] + c[k-1])

    return sorted(res, reverse=True)[:K]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
