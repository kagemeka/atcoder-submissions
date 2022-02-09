import sys

n, *H = map(int, sys.stdin.read().split())

def main():
    ma = 0
    cnt = 0
    for h in H:
        if h >= ma:
            cnt += 1
            ma = h
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
