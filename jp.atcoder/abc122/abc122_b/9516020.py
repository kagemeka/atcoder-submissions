import sys

atcg = set('ATCG')

s = sys.stdin.readline().rstrip()

def main():
    t = s + '$'
    l = len(t)
    res = 0
    cnt = 0
    for i in range(l):
        if t[i] in atcg:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
