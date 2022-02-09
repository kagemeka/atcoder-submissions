import sys

def main():
    s = sys.stdin.readline().rstrip()

    ATCG = set('ATCG')
    res = 0
    cnt = 0
    for char in s:
        if char in ATCG:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
    res = max(res, cnt)

    print(res)

if __name__ == "__main__":
    main()
