import sys

n, m, *ab = map(int, sys.stdin.read().split())
ab = sorted(zip(*[iter(ab)] * 2))

def main():
    cost = 0
    r = m
    for a, b in ab:
        if b <= r:
            cost += a * b
            r -= b
        else:
            cost += a * r
            break
    return cost

if __name__ == '__main__':
    ans = main()
    print(ans)
