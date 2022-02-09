import sys

H, W, N, *cnt_color = map(int, sys.stdin.read().split())

def main():
    canvas = [[None] * W for _ in range(H)]

    h = w = 0
    for i in range(N):
        c = cnt_color[i]
        i = str(i+1)
        for _ in range(c):
            canvas[h][w] = i
            if h & 1:
                w -= 1
                if w == -1:
                    h += 1
                    w = 0
            else:
                w += 1
                if w == W:
                    h += 1
                    w = W - 1

    for i in range(H):
        yield' '.join(canvas[i])

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
