import sys

s = sys.stdin.readline().rstrip() + '+'
l = len(s)

def main():
    cnt = 0
    flag = False
    for i in range(l):
        if i & 1 ^ 1:
            if flag:
                continue
            else:
                if s[i] == '0':
                    flag = True
        else:
            if s[i] == '+':
                if not flag:
                    cnt += 1
                else:
                    flag = False

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
