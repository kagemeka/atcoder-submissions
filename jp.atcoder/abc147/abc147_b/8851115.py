import sys

s = sys.stdin.readline().rstrip()
l = len(s)
def main():
    cnt = 0
    for i in range(l // 2):
        if s[i] != s[-i-1]:
            cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
