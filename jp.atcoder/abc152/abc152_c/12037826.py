import sys

n, *p = map(int, sys.stdin.read().split())

def main():
    m = float('inf')
    cnt = 0
    for x in p:
        if x > m: continue
        cnt += 1
        m = x
    print(cnt)

if __name__ ==  '__main__':
    main()
