import sys
from math import floor, ceil

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def cost(x, y):
    return a * x + c * y

def main():
    costs = []
    for i in range(n, -1, -1):
        # j = floor((n * e - (b + e) * i - h) / (d + e) + 1)
        j = ceil((1 + n * e - (b + e) * i - h) / (d + e))
        if i + j <= n:
            costs.append(cost(i, j))

    return min(costs)

if __name__ == '__main__':
    ans = main()
    print(ans)
