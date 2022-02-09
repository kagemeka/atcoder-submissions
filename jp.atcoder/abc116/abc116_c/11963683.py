import sys

n, *h = map(int, sys.stdin.read().split())

def main():
    cnt = 0
    for _ in range(max(h)):
        flag = 0
        for i in range(n):
            if not h[i]: flag = 0
            else:
                if not flag:
                    flag = 1
                    cnt += 1
                h[i] -= 1
    print(cnt)

if __name__ ==  '__main__':
    main()
