import sys

h, w = map(int, sys.stdin.readline().split())

def main():
    res = h // 2 * w
    if h & 1:
        res += (w + 2 - 1) // 2
    return res

if __name__ == "__main__":
    ans = main()
    print(ans)
