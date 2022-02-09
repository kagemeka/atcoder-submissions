import sys

n, s = sys.stdin.read().split()
n = int(n)

def main():
    if n & 1 ^ 1:
        return -1

    cnt = 0
    for i in range(n // 2 - 1, -1, -1):
        if cnt % 3 == 2:
            if s[i] != 'b' or s[-i-1] != 'b':
                break
        elif cnt % 3 == 0:
            if s[i] != 'a' or s[-i-1] != 'c':
                break
        elif cnt % 3 == 1:
            if s[i] != 'c' or s[-i-1] != 'a':
                break
        cnt += 1
    else:
        return cnt
    return -1

if __name__ == '__main__':
    ans = main()
    print(ans)
