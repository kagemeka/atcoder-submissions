import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())

if x < y:
    x, y = y, x
    a, b = b, a

def main():

    if a + b <= c * 2:
        cost = a * x + b * y
    else:
        cost = c * 2 * y
        if a <= c * 2:
            cost += a * (x - y)
        else:
            cost += c * 2 * (x - y)
    return cost

if __name__ == '__main__':
    ans = main()
    print(ans)
