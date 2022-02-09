import sys

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def cost(x, y):
    return a * x + c * y

def main():
    costs = []
    for i in range(n, -1, -1):
        j = ((n * e - (b + e) * i - h) / (d + e) + 1) // 1
        if i + j <= n:
            costs.append(cost(i, j))

    return int(min(costs))

if __name__ == '__main__':
    ans = main()
    print(ans)
