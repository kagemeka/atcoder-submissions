import sys

x, y, z, k = map(int ,sys.stdin.readline().split())
a, b, c = (sorted(map(int, sys.stdin.readline().split())) for _ in range(3))

def main():
    res = sorted([a[i] + b[j] for i in range(x) for j in range(y)], reverse=True)
    res2 = sorted([res[i] + c[j] for i in range(min(k, x * y)) for j in range(z)], reverse=True)
    return res2[:k]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
