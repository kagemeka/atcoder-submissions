import sys

H, W, h, w = map(int, sys.stdin.read().split())

def main():
    return H * W - (h * W + w * H - h * w)

if __name__ == '__main__':
    ans = main()
    print(ans)
