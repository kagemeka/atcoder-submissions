import sys

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def can_survive(x, y):
    if (b + e) * x + (d + e) * y + h - n * e > 0:
        return True
    return False

def cost(x, y):
    return a * x + c * y

def main():
    costs = []
    for i in range(n, -1, -1):
        j = ((n * e - (b + e) * i - h) / (d + e) + 1) // 1
        costs.append(cost(i, j))

    return min(costs)

if __name__ == '__main__':
    ans = main()
    print(ans)
