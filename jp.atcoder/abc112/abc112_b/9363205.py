import sys

inf = float('inf')

n, T, *ct = map(int, sys.stdin.read().split())
ct = zip(*[iter(ct)] * 2)

def main():
    res = inf
    for c, t in ct:
        if t <= T:
            res = min(res, c)

    return res if res != inf else 'TLE'

if __name__ == '__main__':
    ans = main()
    print(ans)
