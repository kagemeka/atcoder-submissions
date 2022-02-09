import sys

n, s = sys.stdin.read().split()

def main():
    cnt = 0
    prev = '$'
    for c in s:
        if c == prev: continue
        cnt += 1
        prev = c
    print(cnt)

if __name__ ==  '__main__':
    main()
