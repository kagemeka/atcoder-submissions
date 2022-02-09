import sys

n = int(sys.stdin.readline().rstrip())

def main():
    cnt = 0
    for i in range(10):
        q, r = divmod(n, 10 ** (i + 1))
        cnt += 10 ** i * q
        if r >= 10 ** i:
            cnt += min(10 ** i, r + 1 - 10 ** i)

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
