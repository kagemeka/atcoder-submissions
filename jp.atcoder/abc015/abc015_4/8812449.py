import sys

I = [int(x) for x in sys.stdin.read().split()]
W, N, K = I[:3]
width = I[3:][::2]
value = I[3:][1::2]

def main():
    v = [[[0] * (W + 1) for _ in range(K+1)] for _ in range(N+1)]

    for i in range(N):
        for k in range(1, K+1):
            if k > i + 1:
                break
            for w in range(W + 1):
                if width[i] <= w:
                    v[i+1][k][w] = max(v[i][k][w], v[i][k-1][w - width[i]] + value[i])
                else:
                    v[i+1][k][w] = v[i][k][w]
    return v[N][K][W]

if __name__ == '__main__':
    ans = main()
    print(ans)
