import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    s1 = s2 = c1 = c2 = 0
    for i in range(n):
        s1 += a[i]
        s2 += a[i]
        if i & 1:
            if s1 >= 0:
                c1 += abs(-1 - s1)
                s1 = -1

            if s2 <= 0:
                c2 += 1 - s2
                s2 = 1
        else:
            if s1 <= 0:
                c1 += 1 - s1
                s1 = 1

            if s2 >= 0:
                c2 += abs(-1 - s2)
                s2 = -1

    return min(c1, c2)

if __name__ == '__main__':
    ans = main()
    print(ans)
