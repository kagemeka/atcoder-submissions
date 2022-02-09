import sys

inf = float('inf')

n, k, *xy = map(int, sys.stdin.read().split())
xy = list(zip(*[iter(xy)] * 2))

def minimize(xy, key):
    xy = sorted(xy, key=lambda x: x[key])
    x = []
    y = []
    for i in range(n):
        x.append(xy[i][0])
        y.append(xy[i][1])
    if key == 1:
        x, y = y, x

    area = inf
    for i in range(n-k+1):
        l = i; r = i + k - 1
        dx = x[r] - x[l]
        seq_y = sorted(y[l:r+1])
        dy = seq_y[-1] - seq_y[0]
        area = min(area, dx * dy)
    return area

def main():
    return min(minimize(xy, 0), minimize(xy, 1))

if __name__ == '__main__':
    ans = main()
    print(ans)
