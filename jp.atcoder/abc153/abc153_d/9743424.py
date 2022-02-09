import sys

h = int(sys.stdin.readline().rstrip())

def main():
    x = h
    cnt = 0
    while x > 1:
        x //= 2
        cnt += 1
    res = 0
    for i in range(cnt+1):
        res += 2 ** i
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
