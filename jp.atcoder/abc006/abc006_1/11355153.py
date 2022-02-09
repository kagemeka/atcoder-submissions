import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = 'NO'
    if not n % 3:
        ans = 'YES'
    q = n
    while q:
        q, r = divmod(q, 10)
        if r == 3: ans = 'YES'; break
    print(ans)

if __name__ == '__main__':
    main()
