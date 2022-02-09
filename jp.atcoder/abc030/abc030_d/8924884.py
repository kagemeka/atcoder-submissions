import sys

n, a, k, *b = map(int, sys.stdin.read().split())

def main():
    r = k
    fst_occur = [None] * (n + 1)
    fst_occur[a] = 0
    cnt = 0
    i = a
    for _ in range(n):
        i = b[i-1]
        cnt += 1
        if cnt == k:
            return i

        if not fst_occur[i] is None:
            rot_step = cnt - fst_occur[i]
            r -= fst_occur[i]
            r %= rot_step
            break

        fst_occur[i] = cnt

    for _ in range(r):
        i = b[i-1]

    return i

if __name__ == '__main__':
    ans = main()
    print(ans)
