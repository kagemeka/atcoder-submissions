import sys

inf = float('inf')

n, k, *xy = map(int, sys.stdin.read().split())
xy = list(zip(*[iter(xy)] * 2))

def main():
    xy.sort(key=lambda x: x[0])
    x = []
    y = []
    for i in range(n):
        x.append(xy[i][0])
        y.append(xy[i][1])

    area = inf
    for l in range(n-k+1):
        for r in range(l+k-1, n):
            dx = x[r] - x[l]
            seq_y = sorted(y[l:r+1])
            m = r - l + 1
            for d in range(m-k+1):
                for u in range(d+k-1, m):
                    dy = seq_y[u] - seq_y[d]
                    area = min(area, dx * dy)

    return area

if __name__ == '__main__':
    ans = main()
    print(ans)
