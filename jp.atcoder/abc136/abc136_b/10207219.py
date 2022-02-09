import sys

n = sys.stdin.readline().rstrip()
l = len(n)

def main():
    cnt = 0
    for i in range(0, l, 2):
        if i < l-1:
            cnt += 10 ** (i + 1) - 10 ** i
        else:
            cnt += int(n) - (10 ** i - 1)

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
