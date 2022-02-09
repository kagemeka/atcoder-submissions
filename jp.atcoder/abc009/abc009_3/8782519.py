import sys

n, k = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())

def swap(i, j):
    s[i], s[j] = s[j], s[i]

def can_swap(cnt, r):
    if r >= 2 - cnt:
        return True
    return False

def main():
    r = k
    changed = [False] * n
    for _ in range(2):
        for i in range(n-1):
            cand = sorted(c for c in set(s[i+1:]) if c < s[i])
            for c in cand:
                for j in range(n-1, i, -1):
                    if s[j] == c:
                        cnt = changed[i] + changed[j]
                        if can_swap(cnt, r):
                            swap(i, j)
                            r -= 2 - cnt
                            changed[i] = True
                            changed[j] = True
                            break
                else:
                    continue
                break

    ans = ''.join(s)
    print(ans)

if __name__ == '__main__':
    main()
