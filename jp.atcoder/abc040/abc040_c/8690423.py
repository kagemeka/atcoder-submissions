import sys

def main():
    n, *a = map(int, sys.stdin.read().split())
    a = [a[0]] + a
    cost = [None] * (n + 1)
    cost[0], cost[1] = 0, 0
    for i in range(2, n+1):
        cost[i] = min(cost[i-2] + abs(a[i] - a[i-2]), cost[i-1] + abs(a[i] - a[i-1]))

    print(cost[n])

if __name__ == '__main__':
    main()
