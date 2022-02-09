import sys

n, m, v, p, *a = map(int, sys.stdin.read().split())
a.sort(reverse=True)

def possible(i):
    score = a[i] + m
    if i < p:
        return True
    else:
        every_ok = p - 1 + n - i
        if every_ok >= v:
            if score >= a[p-1]:
                return True
            else:
                return False
        else:
            s = m * (v - every_ok)
            limit = 0
            for j in range(p-1, i):
                if a[j] > score:
                    return False
                limit += score - a[j]
            if s > limit:
                return False
            return True

def main():
    lo = -1
    hi = n
    while lo + 1 < hi:
        i = (lo + hi) // 2
        if possible(i):
            lo = i
        else:
            hi = i

    return lo + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
