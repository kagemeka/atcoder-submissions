import sys

n, *h = map(int, sys.stdin.read().split())
h = [h[0]] + h

def main():
    cost = [0] * (n + 1)
    for i in range(2, n + 1):
        cost[i] = min(cost[i-1] + abs(h[i] - h[i-1]), cost[i-2] + abs(h[i] - h[i-2]))
    print(cost[n])

if __name__ ==  '__main__':
    main()
