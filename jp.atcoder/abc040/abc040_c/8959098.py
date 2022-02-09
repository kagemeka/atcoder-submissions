import sys

n, *a = map(int, sys.stdin.read().split())
a.insert(0, a[0])

def main():
    cost = [None] * (n + 1)
    cost[0] = cost[1] = 0
    for i in range(2, n+1):
        c1 = cost[i-2] + abs(a[i] - a[i-2])
        c2 = cost[i-1] + abs(a[i] - a[i-1])
        cost[i] = min(c1, c2)

    return cost[n]

if __name__ == '__main__':
    ans = main()
    print(ans)
