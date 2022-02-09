import sys

n, m, d, *A = map(int, sys.stdin.read().split())

res = list(range(n+1))

def swap(i, j):
    res[i], res[j] = res[j], res[i]

def main():
    for a in reversed(A):
        swap(a, a+1)

    rot = [None] * (n + 1)
    checked = set()
    for i in range(1, n+1):
        if not i in checked:
            group = [i]
            cur = res[i]
            cnt = 1
            while cur != i:
                group.append(cur)
                cur = res[cur]
                cnt += 1

            r = d % cnt
            for j in zip(group, group[r:] + group[:r]):
                rot[j[0]] = j[1]

            checked |= set(group)

    return rot

if __name__ == '__main__':
    ans = main()
    print(*ans[1:], sep='\n')
