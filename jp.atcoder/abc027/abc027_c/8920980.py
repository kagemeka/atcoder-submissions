import sys

n = int(sys.stdin.readline().rstrip())

def main():
    flag = False
    r = n
    if n & 1:
        l = n // 2 + 1
    else:
        l = n // 2
    cnt = 1
    while r > 1:
        if ((l <= 2 <= r) or (l <= 3 <= r)) and cnt & 1:
            flag = True
            break

        if cnt & 1:
            r //= 2
            l //= 2
        else:
            if r & 1:
                r //= 2
            else:
                r = r // 2 - 1

            if l & 1:
                l = l // 2 + 1
            else:
                l // 2

        cnt += 1

    return 'Takahashi' if flag else 'Aoki'

if __name__ == '__main__':
    ans = main()
    print(ans)
