import sys

n, s = sys.stdin.read().split()

def main():
    cnt = s.count('E')
    cur = 'E'
    res = [cnt]
    for c in s:
        if cur == 'W': cnt += 1
        if c == 'E': cnt -= 1
        res.append(cnt)
        cur = c
    print(min(res))

if __name__ ==  '__main__':
    main()
