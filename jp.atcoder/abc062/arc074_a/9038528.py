import sys

H, W = map(int, sys.stdin.readline().split())

def minimize(H, W):
    if H % 3 == 0:
        return 0
    res1 = W
    h = round(H / 3)
    w = W // 2
    block = [h * W, (H - h) * w, (H - h) * (W - w)]
    block.sort()
    res2 = block[-1] - block[0]
    return min(res1, res2)

def main():
    return min(minimize(H, W), minimize(W, H))

if __name__ == '__main__':
    ans = main()
    print(ans)
