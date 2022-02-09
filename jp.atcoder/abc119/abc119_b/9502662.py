import sys

def to_jpy(x, u):
    x = float(x)
    if u == 'BTC':
        x *= 3.8 * 10 ** 5
    return x

n, *xu = sys.stdin.read().split()
xu = zip(*[iter(xu)] * 2)

def main():
    res = 0
    for x, u in xu:
        res += to_jpy(x, u)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
