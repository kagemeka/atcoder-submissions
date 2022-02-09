import sys

H, W, h, w = map(int, sys.stdin.read().split())

def main():
    res = H * W - (h*W + H*w - h*w)
    print(res)

if __name__ ==  '__main__':
    main()
