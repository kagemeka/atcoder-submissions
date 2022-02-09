# 2019-11-25 12:34:24(JST)
import sys
def main():
    n = int(sys.stdin.readline().rstrip())

    # root = 1 とする
    from_1 = []
    for i in range(2, n+1):
        print(f'? {1} {i}')
        sys.stdout.flush
        dist = int(sys.stdin.readline().rstrip())
        from_1.append((dist, i))

    from_1.sort()
    v = from_1[-1][1]
    from_v = []
    for i in range(1, n+1):
        if i != v:
            print(f'? {v} {i}')
            sys.stdout.flush
            dist = int(sys.stdin.readline().rstrip())
            from_v.append((dist, i))

    from_v.sort()
    ans = from_v[-1][0]
    print(ans)

if __name__ == '__main__':
    main()
