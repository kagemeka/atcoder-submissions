import sys

s = sys.stdin.readline().rstrip()

def main():
    prev = '$'
    cnt = -1
    for c in s:
        cnt += c != prev
        prev = c
    print(cnt)

if __name__ ==  '__main__':
    main()
