import sys

H, W = map(int, sys.stdin.readline().split())

def minimize(H, W):
    h = round(H / 3)
    a = h * W
    w = W // 2
    b = (H - h) * w
    c = (H - h) * (W - w)
    return  max(a, b, c) - min(a, b, c)

def main():
    if H % 3 == 0 or W % 3 == 0:
        return 0

    return min(minimize(H, W), minimize(W, H))

if __name__ == '__main__':
    ans = main()
    print(ans)
