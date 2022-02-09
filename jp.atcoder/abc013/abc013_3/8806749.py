import sys

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def cost(x, y):
    return a * x + c * y

def main():
    costs = []
    for x in range(n, -1, -1):
        y = (1 + n * e - (b + e) * x - h + (d + e) - 1) // (d + e)
        if y <= n - x:
            costs.append(cost(x, max(y, 0)))

    return min(costs) if costs else d * n

if __name__ == '__main__':
    ans = main()
    print(ans)
